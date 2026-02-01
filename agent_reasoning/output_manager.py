import logging
from typing import List, Dict, Any
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from .prompts.safety_guardrails import SAFETY_CHECK_PROMPT

logger = logging.getLogger("OutputManager")

class OutputManager:
    def __init__(self, model_name="gpt-4-turbo"):
        self.llm = ChatOpenAI(model=model_name, temperature=0.3)

    def generate_response(self, goal: str, data: dict, layer: str = "summary", tool_trace: List[str] = None) -> str:
        """
        Router for Progressive Disclosure & Traceability.
        
        Layers:
        - 'handover': The "I'm Ready" signal. Used immediately after data processing.
        - 'summary': High-level Executive Summary (BLUF).
        - 'evidence': Detailed answer with Logic Trace (How I found it).
        - 'deep_research': Raw data dump.
        """
        if tool_trace is None:
            tool_trace = []

        logger.info(f"📝 Generating Output. Layer: {layer}")

        if layer == "handover":
            draft = self._generate_handover(goal, data, tool_trace)
        elif layer == "summary":
            draft = self._generate_layer_1(goal, data)
        elif layer == "evidence":
            draft = self._generate_layer_2(goal, data, tool_trace)
        elif layer == "deep_research":
            draft = self._generate_layer_3(data)
        else:
            draft = self._generate_layer_1(goal, data) # Default fallback
            
        return self._apply_safety_check(draft)

    def _generate_handover(self, goal: str, data: dict, tool_trace: List[str]):
        """
        NEW: The 'Ready State' message.
        Does NOT give the full solution. Just summarizes the *effort* and invites questions.
        """
        template = """
        You are a Research Assistant who has just finished processing a dataset.
        
        CONTEXT:
        - Goal: {goal}
        - Tools Ran: {tool_trace}
        - Key Data Points Found: {data_preview}
        
        TASK:
        Write a brief, professional "Handover Message" to the user.
        1. Confirm the analysis is complete.
        2. Mention 2-3 interesting areas you detected (e.g., "I detected a spike in churn" or "I found negative sentiment in pricing").
        3. DO NOT give the full report yet.
        4. End by asking: "Would you like me to start with the Executive Summary, or do you have a specific question?"
        """
        
        # We only show a snippet of data to the LLM for the handover to save tokens
        data_preview = str(data)[:500] 
        
        content = template.format(goal=goal, tool_trace=tool_trace, data_preview=data_preview)
        return self.llm.invoke([HumanMessage(content=content)]).content

    def _generate_layer_1(self, goal, data):
        """Layer 1: The Executive Summary (BLUF)."""
        template = """
        Draft a "Clarity Summary" (Executive Brief).
        
        GOAL: {goal}
        DATA: {data}
        
        RULES:
        1. Start with the Direct Answer / Verdict.
        2. Highlight the #1 Risk clearly.
        3. Use neutral language ("The data suggests...", not "You should...").
        """
        content = template.format(goal=goal, data=str(data)[:1500])
        return self.llm.invoke([HumanMessage(content=content)]).content

    def _generate_layer_2(self, goal, data, tool_trace):
        """
        Layer 2: Evidence & Logic Traceability.
        This answers the user's need for "How did you figure this out?".
        """
        template = """
        You are explaining your research findings in significant detail.
        
        GOAL: {goal}
        DATA FINDINGS: {data}
        RESEARCH STEPS TAKEN: {tool_trace}
        
        INSTRUCTIONS:
        1. **Answer the Question:** Provide a detailed, data-backed answer.
        2. **Show Your Work (Traceability):** - Explicitly mention which numbers you used.
           - Explain the sequence: "First I checked X, which led me to analyze Y..."
           - Example: "I started by running the 'Churn Scan', which flagged a 5% drop. I then cross-referenced this with 'Sentiment Analysis'..."
        3. **Cite Inputs:** Refer to specific user inputs or file columns where possible.
        """
        
        content = template.format(goal=goal, data=str(data)[:3000], tool_trace=tool_trace)
        return self.llm.invoke([HumanMessage(content=content)]).content

    def _generate_layer_3(self, data):
        """Layer 3: Deep Data (Raw)."""
        return f"### 📊 DEEP DATA VIEW\n\n```json\n{data}\n```"

    def _apply_safety_check(self, draft):
        """Runs the safety prompt to scrub prescriptive language."""
        content = SAFETY_CHECK_PROMPT.format(draft=draft)
        return self.llm.invoke([HumanMessage(content=content)]).content
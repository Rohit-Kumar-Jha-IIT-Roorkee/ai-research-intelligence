# agent_reasoning/prompts/safety_guardrails.py

SAFETY_CHECK_PROMPT = """
Review the following agent draft response for strict adherence to safety protocols.

DRAFT:
{draft}

CHECKLIST:
1. Did the agent say "You should" or "I recommend"? -> CHANGE to "The data suggests".
2. Did the agent invent data? -> REMOVE.
3. Is the tone hype-y? -> MAKE NEUTRAL.

Return the REFINED response only.
"""
from data_intelligence.quant_engine import QuantInsightEngine

class ResearchTools:
    """
    The Toolkit Manager that bridges the Agent Brain (Person 1) 
    with the Intelligence Engines (Person 2).
    """
    def __init__(self):
        # Initialize the Quantitative Engine (Person 2)
        self.quant_engine = QuantInsightEngine()

    def analyze_dataset(self, file_path, goal_type="launch"):
        """
        Directly triggers Person 2 to analyze a file based on the goal.
        
        Args:
            file_path (str): Path to the CSV/Excel file.
            goal_type (str): The active goal (e.g., "1. Launch New Product").
            
        Returns:
            str: A formatted markdown report from Person 2.
        """
        # 1. Load Data
        df = self.quant_engine.load_data(file_path)
        
        if df is None:
            return "❌ Error: Could not load data. Please ensure the file exists and is a CSV."

        # 2. Route to correct Goal Function
        # We normalize the string to handle "1. Launch..." or "Launch"
        goal_key = str(goal_type).lower()
        print(f"📊 Tools: Routing Goal '{goal_key}' on {len(df)} rows...")
        
        # --- GOAL 1: LAUNCH ---
        if "launch" in goal_key or "1" in goal_key:
            return self.quant_engine.run_goal_1_analysis(df)
        
        # --- GOAL 2: PERFORMANCE ---
        elif "diagnose" in goal_key or "performance" in goal_key or "2" in goal_key:
            return self.quant_engine.run_goal_2_analysis(df)

        # --- GOAL 3: UX & JOURNEY ---
        elif "ux" in goal_key or "journey" in goal_key or "3" in goal_key:
            return self.quant_engine.run_goal_3_analysis(df)

        # --- GOAL 4: RETENTION ---
        elif "retention" in goal_key or "loyalty" in goal_key or "4" in goal_key:
            return self.quant_engine.run_goal_4_analysis(df)

        # --- GOAL 5: HYPOTHESIS ---
        elif "hypothesis" in goal_key or "test" in goal_key or "5" in goal_key:
            return self.quant_engine.run_goal_5_analysis(df)

        # --- GOAL 6: ROADMAP ---
        elif "roadmap" in goal_key or "priorit" in goal_key or "6" in goal_key:
            return self.quant_engine.run_goal_6_analysis(df)

        # --- GOAL 7: EXECUTIVE SUMMARY ---
        elif "executive" in goal_key or "summary" in goal_key or "7" in goal_key:
            return self.quant_engine.run_goal_7_analysis(df)

        return f"⚠️ Tool not configured for goal: '{goal_type}' yet."

# Legacy support if you still have code calling get_tools_for_goal
def get_tools_for_goal(goal_name: str):
    return []
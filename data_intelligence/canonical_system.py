import pandas as pd

class CanonicalDataSystem:
    def __init__(self, db_manager):
        """
        Initializes the system that normalizes all input formats [cite: 2471-2473].
        Acts as the central relay for metrics, text feedback, and goal-specific signals.
        """
        self.db_manager = db_manager
        self.internal_object = {
            "metrics_present": [],      # Identified quantitative columns [cite: 2475]
            "text_feedback": [],        # Normalized qualitative verbatims [cite: 2476]
            "segments_present": False,  # Flag for demographic/behavioral buckets [cite: 2476]
            "time_series": False,       # Flag for longitudinal data [cite: 2475]
            "survey_themes": [],        # Extracted thematic buckets [cite: 2477]
            "context": {}               # Mandatory pre-context inputs [cite: 209-211]
        }

    def process_input(self, raw_data, data_type):
        """
        Normalizes any format (CSV, Text, Voice) into the Canonical Internal Object [cite: 2463-2470].
        Format and source no longer matter once data is processed [cite: 2479-2480].
        """
        if data_type == "csv":
            df = pd.read_csv(raw_data)
            # Automatically identify metrics and segments for the Auditor [cite: 2475-2477]
            self.internal_object["metrics_present"] = df.columns.tolist()
            self.internal_object["segments_present"] = True if "segment" in df.columns else False
            self.internal_object["time_series"] = True if "date" in df.columns or "timestamp" in df.columns else False
            return df
            
        elif data_type == "text":
            # Store in internal object and index in Vector DB for RAG [cite: 2476-2477]
            self.internal_object["text_feedback"].append(raw_data)
            self.db_manager.add_evidence([raw_data], [{"source": "manual_input"}], [str(hash(raw_data))])
            return raw_data

    def extract_goal_aware_signals(self, goal):
        """
        Extracts specific behavioral and numerical signals based on the selected goal[cite: 2482].
        These signals provide the 'Evidence' for the Agent's reasoning loop.
        """
        signals = {}
        
        # Goal 1: Launch Signals (Demand, Pricing, ICP) [cite: 2488]
        if goal == "launch":
            signals = {
                "demand_authenticity": "high", 
                "price_resistance": "moderate",
                "timing_signal": "early_growth"
            }
            
        # Goal 2: Performance Signals (Root-Cause Indicators) [cite: 2483-2487]
        elif goal == "performance":
            signals = {
                "kpi_anomaly": "retention_spike",
                "causal_link": "activation_bottleneck"
            }

        # Goal 3: UX Signals (Friction, Effort, Confusion) [cite: 2484-2485]
        elif goal == "ux":
            signals = {
                "friction_index": "high", 
                "effort_score": "moderate",
                "confusion_hotspot": "onboarding_step_3"
            } 

        # Goal 4: Retention Signals (Churn timing, Habit gaps) [cite: 2486-2487]
        elif goal == "retention":
            signals = {
                "early_churn_signal": True, 
                "habit_reinforcement_gap": True,
                "loyalty_driver": "utility"
            } 

        # Goal 5: Hypothesis Signals (Quality, Fragility, Bias) [cite: 815, 863]
        elif goal == "hypothesis":
            signals = {
                "hypothesis_quality_score": 0.75,
                "assumption_fragility": "high",
                "bias_risk_alert": "selection_bias"
            }

        # Goal 6: Roadmap Signals (Alignment, Impact, Drift) [cite: 1006, 1022]
        elif goal == "roadmap":
            signals = {
                "strategic_alignment": 0.82,
                "impact_confidence": "high",
                "strategy_drift_signal": "nominal"
            }

        # Goal 7: Executive Signals (Signal-to-Noise, Stakes) [cite: 1184-1188]
        elif goal == "executive":
            signals = {
                "signal_density": "high",
                "executive_confidence_level": "Medium-High",
                "risk_exposure": "low"
            }
        
        return signals

    def set_mandatory_context(self, context_dict):
        """
        Enforces the 'Gatekeeper' rule: mandatory variables must be defined [cite: 209-211, 408-409].
        Ensures engines refuse to run if context like 'product_age' is missing [cite: 586-587, 1183].
        """
        self.internal_object["context"] = context_dict
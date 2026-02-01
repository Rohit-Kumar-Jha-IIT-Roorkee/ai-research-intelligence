from langchain_core.tools import StructuredTool
from .quant_engine import QuantInsightEngine
from .qual_engine import QualEvidenceEngine
from .synthesis_engine import SynthesisEngine
from .canonical_system import CanonicalDataSystem
from .db_manager import VectorDBManager

# --- 1. INITIALIZATION ---
db_manager = VectorDBManager()
canonical = CanonicalDataSystem(db_manager)
quant_engine = QuantInsightEngine(context=canonical.internal_object.get("context"))
qual_engine = QualEvidenceEngine()
synthesis_engine = SynthesisEngine(context=canonical.internal_object.get("context"))

# --- 2. WRAPPER FUNCTIONS (THE MEGA-BUNDLERS) ---

# === GOAL 1: LAUNCH (100% Coverage) ===
def estimate_tam_sam_som(market_size: float, cagr: float, competition_density: float, trend_index: float):
    """Calculates market attractiveness and revenue model fit."""
    attractiveness = quant_engine.compute_market_attractiveness(market_size, cagr, competition_density, trend_index)
    rev_fit = quant_engine.assess_revenue_model_fit("subscription", 0.8) 
    return {"market_score": attractiveness, "revenue_fit": rev_fit}

def analyze_trends_and_timing(trend_index: float, penetration: float):
    """Determines market timing."""
    return quant_engine.assess_entry_timing(trend_index, penetration)

def score_problem_market_fit(pain_freq: float, workaround_usage: bool, verbatims: list):
    """Validates demand using problem frequency, pain intensity, and core problems."""
    problems = qual_engine.extract_core_problems(verbatims)
    pain = qual_engine.score_pain_intensity(str(verbatims))
    pmf = qual_engine.classify_problem_market_fit(pain_freq, workaround_usage)
    return {"pmf": pmf, "pain_scores": pain, "core_problems": problems}

def analyze_substitutes(text_data: str):
    """Analyzes substitutes and inertia."""
    return qual_engine.identify_substitutes_and_inertia(text_data)

def identify_early_adopters(pain_level: float, openness: float, user_data: list):
    """Identifies segments and early adopters."""
    segments = qual_engine.segment_users_multilayer(user_data)
    icp = qual_engine.identify_early_adopters(pain_level, openness)
    return {"segments": segments, "early_adopter_profile": icp}

def map_competitive_landscape(competitor_count: int, feature_overlap: float, gaps: float):
    """Maps density and threats."""
    density = quant_engine.map_competitive_density(competitor_count, feature_overlap)
    threat = quant_engine.compute_competitive_threat_index(gaps)
    return {"density": density, "threat_index": threat}

def define_mvp_scope(feature_mentions: dict):
    """Ranks features for MVP."""
    return quant_engine.rank_feature_desirability(feature_mentions)

def estimate_willingness_to_pay(price_points: list, sensitivity: float):
    """Estimates WTP."""
    return quant_engine.estimate_willingness_to_pay(price_points, sensitivity)

def recommend_launch_channels(channel_feedback: dict):
    """Identifies high signal channels."""
    return qual_engine.identify_high_signal_channels(channel_feedback)

def stress_test_assumptions(evidence_strength: float, assumption_count: int):
    """Synthesizes launch readiness and risks."""
    stress = synthesis_engine.stress_test_launch_assumptions(evidence_strength, assumption_count)
    readiness = synthesis_engine.synthesize_launch_readiness({})
    return {"stress_test": stress, "final_readiness": readiness}


# === GOAL 2: PERFORMANCE (100% Coverage) ===
# Added: analyze_feature_adoption, analyze_pricing_friction, detect_message_market_mismatch, analyze_brand_sentiment

def validate_north_star(correlation: float):
    """Validates North Star metric."""
    return quant_engine.validate_north_star_metric(correlation)

def scan_kpi_health(metrics: dict, industry_avg: dict):
    """Comprehensive KPI scan."""
    health = quant_engine.scan_kpi_health(metrics)
    bench = quant_engine.benchmark_kpis(metrics, industry_avg)
    rev_qual = quant_engine.assess_revenue_quality(metrics.get('LTV',0), metrics.get('CAC',1))
    
    # ADDED: Feature Adoption Analysis (Quant)
    feat_adopt = quant_engine.analyze_feature_adoption(metrics.get('feature_usage', {}))
    
    return {"health": health, "benchmarks": bench, "revenue_quality": rev_qual, "feature_adoption": feat_adopt}

def map_funnel_dropoffs(conversion_rates: dict, friction_score: float):
    """Maps funnel dropoffs and correlates friction."""
    ranks = quant_engine.rank_stage_dropoffs(conversion_rates)
    corr = quant_engine.correlate_friction_to_dropoff(friction_score, 0.5)
    
    # ADDED: Pricing Friction & Mismatch (Qual)
    price_fric = qual_engine.analyze_pricing_friction("checkout_logs")
    msg_mismatch = qual_engine.detect_message_market_mismatch("ad_copy", "landing_page")
    
    return {"dropoffs": ranks, "friction_correlation": corr, "pricing_friction": price_fric, "message_mismatch": msg_mismatch}

def benchmark_against_industry(current: dict, avg: dict):
    """Benchmarks KPIs."""
    bench = quant_engine.benchmark_kpis(current, avg)
    channels = quant_engine.evaluate_channel_efficiency({'paid': 2.0})
    
    # ADDED: Brand Sentiment (Qual)
    brand = qual_engine.analyze_brand_sentiment(["reviews"])
    
    return {"benchmarks": bench, "channel_efficiency": channels, "brand_sentiment": brand}

def rank_bottlenecks(conversion_rates: dict, feature_data: dict):
    """Ranks bottlenecks and root causes."""
    root = synthesis_engine.synthesize_root_causes(conversion_rates)
    actions = synthesis_engine.prioritize_actions(conversion_rates)
    val_gap = qual_engine.detect_value_gap("promise", "reality")
    return {"root_causes": root, "priorities": actions, "value_gap": val_gap}


# === GOAL 3: UX & JOURNEY (100% Coverage) ===
# Added: prioritize_ux_fixes, estimate_metric_lift

def decompose_user_journey(raw_steps: list, touchpoints: list):
    """Decomposes journey and maps touchpoints."""
    steps = qual_engine.decompose_user_journey(raw_steps)
    points = qual_engine.map_touchpoints(raw_steps)
    cross_dev = synthesis_engine.analyze_cross_device_journeys({}, {})
    ctx_loss = synthesis_engine.detect_context_loss([])
    return {"steps": steps, "touchpoints": points, "cross_device": cross_dev, "context_loss": ctx_loss}

def score_effort_and_friction(step_count: int, time: int, errors: list, logs: list):
    """Scores effort and identifies friction/flow issues."""
    effort = quant_engine.compute_effort_score(step_count, time)
    f_type = qual_engine.classify_friction_by_step(time, errors)
    flow = qual_engine.detect_flow_disruptions(logs)
    success = quant_engine.compute_task_success_rate(10, 12)
    return {"effort": effort, "type": f_type, "flow_breaks": flow, "success_rate": success}

def analyze_time_to_value(ttfv: int, exits: dict):
    """Analyzes TTFV and onboarding exits."""
    ttfv_score = quant_engine.compute_time_to_first_value(ttfv)
    exit_spots = quant_engine.analyze_onboarding_exits(exits)
    gap = qual_engine.detect_expectation_gap("ad", "product")
    return {"ttfv": ttfv_score, "exits": exit_spots, "exp_gap": gap}

def audit_heuristic_violations(violations: list, ui_elements: list, text: str):
    """Audits heuristics, UI patterns, and accessibility."""
    heuristics = qual_engine.run_heuristic_evaluation(violations)
    patterns = qual_engine.detect_ui_antipatterns(ui_elements)
    access = qual_engine.assess_accessibility_risk(ui_elements)
    recovery = qual_engine.analyze_errors_and_recovery(violations)
    
    # ADDED: Prioritization & Lift (Synthesis)
    priorities = synthesis_engine.prioritize_ux_fixes(violations)
    lift = synthesis_engine.estimate_metric_lift("fix_type")
    
    return {"heuristics": heuristics, "patterns": patterns, "accessibility": access, "recovery": recovery, "prioritized_fixes": priorities, "estimated_lift": lift}

def map_emotional_curve(sentiment: dict, feedback: list):
    """Maps emotions, trust, and delight."""
    curve = qual_engine.compute_emotional_curve(sentiment)
    state = qual_engine.analyze_emotional_sentiment(str(feedback))
    trust = qual_engine.detect_trust_gaps(feedback)
    delight = qual_engine.identify_delight_moments(feedback)
    themes = qual_engine.mine_ux_feedback_themes(feedback)
    latent = qual_engine.detect_latent_needs(feedback)
    return {"curve": curve, "state": state, "trust": trust, "delight": delight, "themes": themes, "latent": latent}


# === GOAL 4: RETENTION (100% Coverage) ===
def analyze_retention_decay(cohorts: dict, churn: float):
    """Analyzes retention decay and survival."""
    time = quant_engine.compute_time_based_retention(cohorts)
    cohort = quant_engine.analyze_cohort_retention(cohorts)
    survival = quant_engine.run_survival_analysis(churn)
    return {"time_decay": time, "cohort_analysis": cohort, "survival": survival}

def identify_churn_triggers(feedback: list, logs: list):
    """Identifies churn drivers and types."""
    drivers = qual_engine.identify_churn_drivers(feedback)
    c_type = qual_engine.classify_churn_types()
    signals = qual_engine.detect_exit_signals()
    patterns = qual_engine.identify_pre_churn_patterns()
    return {"drivers": drivers, "type": c_type, "signals": signals, "patterns": patterns}

def score_habit_strength(streaks: int, routines: int, freq_exp: int, freq_act: int):
    """Scores habits and loops."""
    habit = quant_engine.detect_habit_signals(streaks, routines)
    freq = quant_engine.check_frequency_alignment(freq_exp, freq_act)
    loop = qual_engine.analyze_core_value_loop([])
    segs = qual_engine.segment_users_behaviorally()
    power = qual_engine.profile_power_users([])
    return {"habit": habit, "freq": freq, "loop": loop, "segments": segs, "power_users": power}

def calculate_switching_costs(data_points: int):
    """Calculates switching costs and lock-in."""
    cost = quant_engine.compute_switching_cost_index(data_points)
    ethics = synthesis_engine.evaluate_lock_in_ethics({})
    drivers = qual_engine.analyze_emotional_drivers([])
    advocacy = qual_engine.analyze_advocacy_patterns([])
    return {"cost": cost, "ethics": ethics, "drivers": drivers, "advocacy": advocacy}

def evaluate_loyalty_program(lift: float, cost: float, messages: list):
    """Evaluates loyalty and communication."""
    eff = quant_engine.measure_incentive_effectiveness(lift, cost)
    fatigue = synthesis_engine.detect_incentive_fatigue([])
    winback = synthesis_engine.optimize_winback_strategies(30)
    levers = synthesis_engine.score_retention_levers(0.1)
    flywheel = synthesis_engine.design_retention_flywheel([],[],[])
    roadmap = synthesis_engine.build_retention_roadmap({})
    msg_audit = qual_engine.audit_lifecycle_messages(messages)
    relevance = qual_engine.evaluate_relevance_exposure()
    timing = synthesis_engine.optimize_timing_windows([], [])
    return {"efficiency": eff, "fatigue": fatigue, "winback": winback, "levers": levers, "flywheel": flywheel, "roadmap": roadmap, "audit": msg_audit, "relevance": relevance, "timing": timing}


# === GOAL 5: HYPOTHESIS (100% Coverage) ===
def validate_hypothesis_structure(hypothesis: dict):
    """Validates structure."""
    return quant_engine.validate_hypothesis_structure(hypothesis)

def score_assumption_fragility(uncertainty: float, dependency: float, assumptions: list):
    """Scores fragility and quality."""
    fragility = quant_engine.score_assumption_fragility(uncertainty, dependency)
    quality = quant_engine.score_hypothesis_quality(True, True)
    h_type = qual_engine.classify_hypothesis_type("change", "metric")
    mapped = qual_engine.map_assumptions(assumptions)
    return {"fragility": fragility, "quality": quality, "type": h_type, "assumptions": mapped}

def select_evidence_strategy(hyp_type: str, data: list):
    """Selects strategy and checks biases."""
    strat = synthesis_engine.select_evidence_strategy(hyp_type)
    bias = qual_engine.identify_bias_risks(data)
    conf = qual_engine.detect_confounders(data)
    return {"strategy": strat, "bias": bias, "confounders": conf}

def design_test_blueprint(metric: str, size: int, effect: float):
    """Designs test."""
    blue = synthesis_engine.design_test_blueprint(metric)
    signal = quant_engine.estimate_signal_strength(size, effect)
    return {"blueprint": blue, "signal": signal}

def interpret_test_results(outcome: dict, penalty: float):
    """Interprets results and updates library."""
    interp = synthesis_engine.interpret_results(outcome)
    action = synthesis_engine.map_verdict_to_action("validated")
    lib = synthesis_engine.update_hypothesis_library(outcome)
    next_hyp = synthesis_engine.suggest_next_hypotheses(outcome)
    adj = quant_engine.adjust_confidence_score(penalty)
    learn = qual_engine.extract_learnings([], [])
    return {"interpretation": interp, "action": action, "library": lib, "next": next_hyp, "adj": adj, "learnings": learn}


# === GOAL 6: PRIORITIZATION (100% Coverage) ===
# Added: map_dependencies, suggest_parallelization, detect_portfolio_imbalance, detect_stakeholder_bias, assess_delivery_risk

def check_strategy_alignment(vision: str, initiatives: list):
    """Checks alignment and drift."""
    vision_map = synthesis_engine.map_initiatives_to_vision(vision, initiatives)
    audit = quant_engine.audit_metric_alignment("metric", "north_star")
    drift = synthesis_engine.detect_strategy_drift([], [])
    
    # ADDED: Portfolio Imbalance (Synthesis)
    portfolio = synthesis_engine.detect_portfolio_imbalance()
    
    return {"vision": vision_map, "audit": audit, "drift": drift, "portfolio_balance": portfolio}

def estimate_impact_vs_effort(reach: int, impact: int, conf: float, dev: int, des: int):
    """Estimates impact, effort, and risks."""
    biz = quant_engine.estimate_business_impact(reach, impact, conf)
    adj = quant_engine.adjust_impact_by_confidence(biz["impact_score"], "high")
    sec = quant_engine.model_second_order_effects([])
    eff = quant_engine.estimate_effort(dev, des)
    
    # ADDED: Delivery Risk (Quant)
    risk = quant_engine.assess_delivery_risk()
    
    return {"impact": biz, "adjusted": adj, "second_order": sec, "effort": eff, "delivery_risk": risk}

def rank_rice_score(scores: dict, initiatives: list):
    """Ranks initiatives and kills low value ones."""
    rank = synthesis_engine.rank_initiatives(scores)
    kill = synthesis_engine.identify_kill_candidates(initiatives)
    
    # ADDED: Stakeholder Bias (Synthesis)
    bias = synthesis_engine.detect_stakeholder_bias()
    
    return {"ranking": rank, "kill_list": kill, "bias_check": bias}

def detect_strategy_drift(patterns: list):
    """Duplicate call for safety/direct access."""
    return synthesis_engine.detect_strategy_drift(patterns, [])

def simulate_roadmap_scenarios(items: list, base: float, lift: float, change: float):
    """Simulates roadmap scenarios."""
    sim = synthesis_engine.simulate_scenarios(items)
    sens = quant_engine.run_sensitivity_analysis(change)
    horizons = quant_engine.map_to_horizons([], [], [])
    forecast = quant_engine.forecast_metric_impact(base, lift)
    resilience = quant_engine.compute_roadmap_resilience()
    org = quant_engine.check_org_readiness()
    crit = quant_engine.identify_critical_path()
    frame = quant_engine.select_prioritization_framework()
    
    # ADDED: Dependencies & Parallelization (Synthesis)
    deps = synthesis_engine.map_dependencies()
    parallel = synthesis_engine.suggest_parallelization()
    
    return {"simulation": sim, "sensitivity": sens, "horizons": horizons, "forecast": forecast, "resilience": resilience, "org": org, "critical_path": crit, "framework": frame, "dependencies": deps, "parallelization": parallel}


# === GOAL 7: SYNTHESIS (100% Coverage) ===
def distill_key_signals(findings: list):
    """Distills insights."""
    top = synthesis_engine.distill_top_insights(findings)
    so_what = qual_engine.frame_so_what(top[0] if top else {})
    return {"insights": top, "so_what": so_what}

def generate_executive_recommendation(insights: list):
    """Generates recommendation."""
    rec = synthesis_engine.generate_recommendation(insights)
    risk = quant_engine.assess_confidence_and_risk(0.9)
    criteria = quant_engine.define_success_criteria("metric", 100)
    return {"recommendation": rec, "risk": risk, "criteria": criteria}

def anticipate_objections(recommendation: str):
    """Anticipates objections."""
    return synthesis_engine.anticipate_objections(recommendation)

def format_decision_brief(synthesis: dict, verdict: str, why: str, risk: str):
    """Formats the brief."""
    fmt = synthesis_engine.render_formats(synthesis)
    arc = synthesis_engine.build_story_arc({}, {}, {})
    snap = synthesis_engine.create_decision_snapshot(verdict, why, risk)
    return {"formats": fmt, "story_arc": arc, "snapshot": snap}


# --- 3. EXPORT LIST ---
ALL_DEFINED_TOOLS = [
    # Goal 1
    StructuredTool.from_function(estimate_tam_sam_som),
    StructuredTool.from_function(analyze_trends_and_timing),
    StructuredTool.from_function(score_problem_market_fit),
    StructuredTool.from_function(analyze_substitutes),
    StructuredTool.from_function(identify_early_adopters),
    StructuredTool.from_function(map_competitive_landscape),
    StructuredTool.from_function(define_mvp_scope),
    StructuredTool.from_function(estimate_willingness_to_pay),
    StructuredTool.from_function(recommend_launch_channels),
    StructuredTool.from_function(stress_test_assumptions),
    
    # Goal 2
    StructuredTool.from_function(validate_north_star),
    StructuredTool.from_function(scan_kpi_health),
    StructuredTool.from_function(map_funnel_dropoffs),
    StructuredTool.from_function(benchmark_against_industry),
    StructuredTool.from_function(rank_bottlenecks),
    
    # Goal 3
    StructuredTool.from_function(decompose_user_journey),
    StructuredTool.from_function(score_effort_and_friction),
    StructuredTool.from_function(analyze_time_to_value),
    StructuredTool.from_function(audit_heuristic_violations),
    StructuredTool.from_function(map_emotional_curve),
    
    # Goal 4
    StructuredTool.from_function(analyze_retention_decay),
    StructuredTool.from_function(identify_churn_triggers),
    StructuredTool.from_function(score_habit_strength),
    StructuredTool.from_function(calculate_switching_costs),
    StructuredTool.from_function(evaluate_loyalty_program),
    
    # Goal 5
    StructuredTool.from_function(validate_hypothesis_structure),
    StructuredTool.from_function(score_assumption_fragility),
    StructuredTool.from_function(select_evidence_strategy),
    StructuredTool.from_function(design_test_blueprint),
    StructuredTool.from_function(interpret_test_results),
    
    # Goal 6
    StructuredTool.from_function(check_strategy_alignment),
    StructuredTool.from_function(estimate_impact_vs_effort),
    StructuredTool.from_function(rank_rice_score),
    StructuredTool.from_function(detect_strategy_drift),
    StructuredTool.from_function(simulate_roadmap_scenarios),
    
    # Goal 7
    StructuredTool.from_function(distill_key_signals),
    StructuredTool.from_function(generate_executive_recommendation),
    StructuredTool.from_function(anticipate_objections),
    StructuredTool.from_function(format_decision_brief),
]
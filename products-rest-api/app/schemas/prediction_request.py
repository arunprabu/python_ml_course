from pydantic import BaseModel


class PredictionRequest(BaseModel):
    # --- Raw customer attributes (required) ---
    age: int
    gender: str
    tenure_months: int
    subscription_plan: str
    monthly_charges: float
    total_charges: float
    contract_type: str
    payment_method: str
    login_frequency_monthly: int
    features_used: int
    data_consumption_gb: float
    engagement_score: float
    days_since_last_activity: int
    billing_issues_count: int
    plan_changes: int
    support_tickets: int
    avg_resolution_hours: float
    satisfaction_score: float
    nps_score: float

    # --- Engineered features (optional; derived from the raw attributes) ---
    monthly_value_ratio: float | None = None
    charge_per_feature: float | None = None
    customer_lifetime_value: float | None = None
    value_tier: str | None = None
    engagement_velocity: float | None = None
    login_intensity: float | None = None
    data_per_login: float | None = None
    activity_recency_category: str | None = None
    features_utilization_rate: float | None = None
    data_per_tenure: float | None = None
    support_rate_annual: float | None = None
    resolution_burden: float | None = None
    satisfaction_gap: float | None = None
    billing_risk_flag: int | None = None
    complaint_ratio: float | None = None
    support_satisfaction_ratio: float | None = None
    nps_category: str | None = None
    plan_tenure_mismatch: int | None = None
    usage_plan_mismatch: int | None = None
    payment_stability: float | None = None
    nps_satisfaction_alignment: float | None = None
    contract_value_risk: int | None = None
    lifecycle_stage: str | None = None
    contract_tenure_ratio: float | None = None
    tenure_category: str | None = None
    engagement_growth_rate: float | None = None
    tenure_stability: float | None = None

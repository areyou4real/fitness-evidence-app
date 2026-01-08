import pandas as pd

from services.trend_service import get_strength_data, get_bodyweight_data
from logic.strength_metrics import strength_trend_percent
from logic.bodyweight_metrics import bodyweight_slope
from logic.scoring import confidence_score


def generate_evidence(user_id):
    evidence = {}

    strength_df = get_strength_data(user_id)
    bw_df = get_bodyweight_data(user_id)

    # Strength
    if not strength_df.empty:
        grouped = strength_df.groupby("exercise")["volume_load"].mean()
        strength_pct = strength_trend_percent(grouped.values)
    else:
        strength_pct = 0

    # Bodyweight
    if len(bw_df) >= 5:
        slope = bodyweight_slope(
            bw_df["log_date"], bw_df["weight"]
        )
    else:
        slope = 0

    evidence["strength_pct"] = strength_pct
    evidence["weight_slope"] = slope

    evidence["confidence"] = confidence_score(
        strength_pct=strength_pct,
        weight_slope=slope,
        volume_ok=True,  # placeholder until volume page
    )

    return evidence

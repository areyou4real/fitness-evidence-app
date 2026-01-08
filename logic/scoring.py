def confidence_score(strength_pct, weight_slope, volume_ok):
    """
    Returns confidence level: green / yellow / red
    """

    score = 0

    # Strength
    if strength_pct > 2:
        score += 2
    elif strength_pct > 0:
        score += 1

    # Bodyweight direction consistency
    if abs(weight_slope) > 0.01:
        score += 1

    # Volume
    if volume_ok:
        score += 1

    if score >= 4:
        return "high"
    elif score >= 2:
        return "medium"
    else:
        return "low"

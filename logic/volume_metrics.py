VOLUME_THRESHOLDS = {
    "chest": (8, 20),
    "back": (8, 20),
    "quads": (8, 20),
    "hamstrings": (6, 16),
    "shoulders": (6, 16),
    "biceps": (6, 16),
    "triceps": (6, 16),
}


def volume_status(weekly_sets, muscle):
    """
    Returns 'low', 'adequate', or 'high'
    """
    if muscle not in VOLUME_THRESHOLDS:
        return "unknown"

    low, high = VOLUME_THRESHOLDS[muscle]

    if weekly_sets < low:
        return "low"
    elif weekly_sets > high:
        return "high"
    else:
        return "adequate"

import numpy as np


def strength_trend_percent(values):
    """
    Returns % change from first to last rolling value.
    """
    if len(values) < 2:
        return 0.0

    start = values[0]
    end = values[-1]

    if start == 0:
        return 0.0

    return ((end - start) / start) * 100

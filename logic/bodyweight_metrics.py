import numpy as np


def bodyweight_slope(dates, weights):
    """
    Returns slope of weight change per day.
    """
    if len(weights) < 2:
        return 0.0

    x = np.arange(len(weights))
    y = np.array(weights)

    slope = np.polyfit(x, y, 1)[0]
    return slope

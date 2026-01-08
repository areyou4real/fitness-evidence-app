def rolling_average(series, window=7):
    return series.rolling(window=window, min_periods=1).mean()

import numpy as np

def RSI(series, period=14):
    delta = series.diff().dropna()
    ups = delta * 0
    downs = ups.copy()
    ups[delta > 0] = delta[delta > 0]
    downs[delta < 0] = -delta[delta < 0]
    ups[ups.index[period-1]] = np.mean(ups[:period])
    ups = ups.drop(ups.index[:(period-1)])
    downs[downs.index[period-1]] = np.mean(downs[:period])
    downs = downs.drop(downs.index[:(period-1)])
    rs = ups.ewm(com=period-1, min_periods=0, adjust=False, ignore_na=False).mean() / \
         downs.ewm(com=period-1, min_periods=0, adjust=False, ignore_na=False).mean()
    return 100 - 100 / (1 + rs)

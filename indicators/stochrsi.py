import numpy as np
from .rsi import RSI

def StochRSI(series, period=14, smoothK=3, smoothD=3):
    rsi = RSI(series, period)
    stochrsi = (rsi - rsi.rolling(period).min()) / (rsi.rolling(period).max() - rsi.rolling(period).min())
    stochrsi_k = stochrsi.rolling(smoothK).mean() * 100
    stochrsi_d = stochrsi_k.rolling(smoothD).mean()
    return stochrsi_k, stochrsi_d
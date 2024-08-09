def calculate_ema(df, span):
    return df.ewm(span=span, adjust=False).mean()

def calculate_macd(df, fastperiod=12, slowperiod=26, signalperiod=9):
    ema_fast = calculate_ema(df['close'], fastperiod)
    ema_slow = calculate_ema(df['close'], slowperiod)
    macd = ema_fast - ema_slow
    macd_signal = calculate_ema(macd, signalperiod)
    macd_hist = macd - macd_signal
    
    return macd, macd_signal, macd_hist
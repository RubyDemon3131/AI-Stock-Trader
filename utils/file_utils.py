import os
import csv
from pathlib import Path
import logging
from tvDatafeed import TvDatafeedLive, Interval as TVInterval

data_dir = "data"
config_dir = "config"
username = ''  # Add your TradingView username here
password = ''  # Add your TradingView password here

# Initialize the TradingView API
tvl = TvDatafeedLive(username, password)

def fetch_initial_data(symbol, exchange, ohlcv_file):
    """Fetch initial data and save it to the OHLCV file."""
    try:
        logging.info(f"Fetching initial data for {symbol} on {exchange}...")
        data = tvl.get_hist(symbol, exchange, interval=TVInterval.in_1_minute, n_bars=240, fut_contract=None, extended_session=False, timeout=-1)
        if data is None:
            logging.error("Failed to fetch initial data")
            return

        data.reset_index(inplace=True)
        data.rename(columns={'datetime': 'date'}, inplace=True)
        data['date'] = data['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
        data = data[['date', 'open', 'high', 'low', 'close', 'volume']]

        # Calculate the indicators
        from trading_strategy import TradingStrategy
        strategy = TradingStrategy()  # Assume default strategy or load from a config
        data = strategy.calculate_indicators(data)

        data.to_csv(ohlcv_file, index=False)
        logging.info(f"Initial data saved to {ohlcv_file}")

    except Exception as e:
        logging.error(f"Error in fetching initial data: {e}")

def setup_file_paths(filename, symbol, exchange):
    ohlcv_file = os.path.join(data_dir, f"{filename}_Real_Time_OHLCV.csv")
    signal_system_file = os.path.join(data_dir, f"{filename}_Signal_system.csv")

    # Check if the OHLCV file exists, if not, fetch initial data
    if not Path(ohlcv_file).is_file():
        logging.info(f"{ohlcv_file} not found, fetching initial data...")
        fetch_initial_data(symbol, exchange, ohlcv_file)

    return ohlcv_file, signal_system_file

def get_strategy_config_file():
    """Return the path to the strategy configuration file."""
    return os.path.join(config_dir, "strategy_config.json")

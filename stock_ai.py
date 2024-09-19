import logging
from threading import Thread
from modules.chart_drawer import draw_chart, update_chart_and_indicators
from modules.data_fetcher import start_data_fetching
from utils.file_utils import setup_file_paths, get_strategy_config_file
import sys

def main(symbol, exchange, title, filename):
    logging.info("Starting the application...")

    # Set up file paths based on the given filename, symbol, and exchange
    ohlcv_file, signal_system_file = setup_file_paths(filename, symbol, exchange)

    # Get the strategy config file path
    strategy_config_file = get_strategy_config_file()

    # Initialize the chart with the provided title
    chart, rsi_line, macd_line, macd_signal_line, macd_histogram_series, stochrsi_k_line, stochrsi_d_line = draw_chart(title, ohlcv_file)

    # Start the update thread for the chart indicators
    update_thread = Thread(target=update_chart_and_indicators, args=(chart, rsi_line, macd_line, macd_signal_line, macd_histogram_series, stochrsi_k_line, stochrsi_d_line, ohlcv_file))
    update_thread.start()

    # Start data fetching for the given symbol and exchange
    start_data_fetching(chart, signal_system_file, symbol, exchange, strategy_config_file)

    chart.show(block=True)

if __name__ == '__main__':
    # Extract command-line arguments
    symbol = sys.argv[1]
    exchange = sys.argv[2]
    title = sys.argv[3]
    filename = sys.argv[4]
    
    # Run the main function with the arguments
    main(symbol, exchange, title, filename)

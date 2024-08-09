import pandas as pd
from indicators.rsi import RSI
from indicators.macd import calculate_macd
from indicators.stochrsi import StochRSI
import json
import logging

class TradingStrategy:
    def __init__(self, config_file):
        # Load strategy parameters from JSON config file
        with open(config_file, 'r') as f:
            config = json.load(f)
        
        self.take_profit = config.get('take_profit', 2.0)
        self.stop_loss = config.get('stop_loss', 1.0)
        self.rsi_period = config.get('rsi_period', 14)
        self.stochrsi_period = config.get('stochrsi_period', 14)
        self.macd_fast_period = config.get('macd_fast_period', 12)
        self.macd_slow_period = config.get('macd_slow_period', 26)
        self.macd_signal_period = config.get('macd_signal_period', 9)
        self.trade_open = False
        self.entry_price = None
        self.signal_records = []

        # Default RSI and StochRSI ranges
        self.rsi_overbought = config.get('rsi_overbought', 70)
        self.rsi_oversold = config.get('rsi_oversold', 30)
        self.stochrsi_overbought = config.get('stochrsi_overbought', 80)
        self.stochrsi_oversold = config.get('stochrsi_oversold', 20)

    def calculate_indicators(self, df):
        # Ensure there is enough data to calculate indicators
        if len(df) < max(self.rsi_period, self.macd_slow_period, self.stochrsi_period):
            logging.error(f"Not enough data to calculate indicators. Required: {max(self.rsi_period, self.macd_slow_period, self.stochrsi_period)}, Available: {len(df)}")
            return df  # Return the DataFrame as is without adding indicators
        
        # Calculate indicators based on the set periods
        df['rsi'] = RSI(df['close'], self.rsi_period)
        df['macd'], df['macd_signal'], df['macd_hist'] = calculate_macd(df, self.macd_fast_period, self.macd_slow_period, self.macd_signal_period)
        df['stochrsi_K'], df['stochrsi_D'] = StochRSI(df['close'], self.stochrsi_period)
        
        return df


    def generate_signals(self, df, chart, signal_system_file, ohlcv_file, last_processed_index=None):
        # Ensure the signal column exists
        if 'signal' not in df.columns:
            df['signal'] = 'Hold'  # Default all to 'Hold'

        # Process only new data
        if last_processed_index is not None:
            new_data = df.iloc[last_processed_index + 1:].reset_index(drop=True)
        else:
            new_data = df

        for i in range(1, len(new_data)):
            current_signal = 'Hold'

            stochrsi_tendency_up = new_data.loc[i, 'stochrsi_K'] > new_data.loc[i-1, 'stochrsi_K']
            stochrsi_tendency_down = new_data.loc[i, 'stochrsi_K'] < new_data.loc[i-1, 'stochrsi_K']
            rsi_tendency_up = new_data.loc[i, 'rsi'] > new_data.loc[i-1, 'rsi']
            rsi_tendency_down = new_data.loc[i, 'rsi'] < new_data.loc[i-1, 'rsi']

            stochrsi_range_up = new_data.loc[i, 'stochrsi_K'] < self.stochrsi_overbought
            stochrsi_range_down = new_data.loc[i, 'stochrsi_K'] > self.stochrsi_oversold
            rsi_range_up = new_data.loc[i, 'rsi'] < self.rsi_overbought
            rsi_range_down = new_data.loc[i, 'rsi'] > self.rsi_oversold

            open_trade_condition = (stochrsi_tendency_up and rsi_tendency_up and stochrsi_range_up and rsi_range_up) or \
                                (new_data.loc[i, 'macd'] > new_data.loc[i, 'macd_signal'] and new_data.loc[i-1, 'macd'] <= new_data.loc[i-1, 'macd_signal'])
            close_trade_condition = (stochrsi_tendency_down and rsi_tendency_down and stochrsi_range_down and rsi_range_down) or \
                                    (new_data.loc[i, 'macd'] < new_data.loc[i, 'macd_signal'] and new_data.loc[i-1, 'macd'] >= new_data.loc[i-1, 'macd_signal'])

            if open_trade_condition and not self.trade_open:
                new_data.loc[i, 'signal'] = 'Open Trade'
                self.trade_open = True
                self.entry_price = new_data.loc[i, 'close']
                self.signal_records.append({
                    'Buy Time': new_data.loc[i, 'date'],
                    'Buy Price': self.entry_price,
                    'Take Profit': self.entry_price + (self.entry_price * (self.take_profit / 100)),  # Adjusted for percentage
                    'Stop Loss': self.entry_price - (self.entry_price * (self.stop_loss / 100)),  # Adjusted for percentage
                    'Close': None,
                    'Close Time': None
                })
                chart.marker(time=new_data.loc[i, 'date'], position='below', shape='arrowUp', color='green', text='Open Trade!')
                print("Signal: Open Trade!")
            elif close_trade_condition and self.trade_open:
                new_data.loc[i, 'signal'] = 'Close Trade'
                self.trade_open = False
                for signal in self.signal_records:
                    if signal['Close'] is None:
                        signal['Close'] = new_data.loc[i, 'close']
                        signal['Close Time'] = new_data.loc[i, 'date']
                        profit_loss = (signal['Close'] - signal['Buy Price']) / signal['Buy Price'] * 100
                        signal['%'] = f"{profit_loss:.2f}%"
                        chart.marker(time=new_data.loc[i, 'date'], position='above', shape='arrowDown', color='red', text=f"Close Trade ({signal['%']})")
                        print(f"Signal: Close Trade at {new_data.loc[i, 'date']} with P&L {signal['%']}")
                        break  # Only close one trade at a time

        # Load existing data from the CSV file
        try:
            existing_data = pd.read_csv(ohlcv_file)
            combined_data = pd.concat([existing_data, new_data]).drop_duplicates(subset='date', keep='last').reset_index(drop=True)
        except FileNotFoundError:
            combined_data = new_data

        print("Saving updated dataframe")
        combined_data.to_csv(ohlcv_file, index=False)

        # Save the signals
        signal_df = pd.DataFrame(self.signal_records)
        
        if not signal_df.empty:
            try:
                # Load existing data from the signal system file
                existing_signals = pd.read_csv(signal_system_file)
                
                # Remove duplicates by comparing 'Buy Time' and 'Close Time'
                signal_df = signal_df[~signal_df[['Buy Time', 'Close Time']].apply(tuple, axis=1).isin(
                    existing_signals[['Buy Time', 'Close Time']].apply(tuple, axis=1))]
                
            except FileNotFoundError:
                # If the file does not exist, there are no existing signals to compare with
                logging.info(f"{signal_system_file} not found. No existing signals to compare.")
            
            if not signal_df.empty:
                # Append the filtered signal_df to the signal system file
                with open(signal_system_file, mode='a', newline='') as file:
                    signal_df.to_csv(file, header=file.tell()==0, index=False)
                print(f"Signals saved to {signal_system_file}.")
            else:
                print(f"No new signals to save to {signal_system_file}.")
        else:
            print(f"No signals to save to {signal_system_file}.")


        return len(df) - 1


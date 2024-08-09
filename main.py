import csv
import subprocess
import os
import sys
import pandas as pd

def get_virtual_env_python():
    """Return the path to the Python interpreter in the current virtual environment."""
    return sys.executable

def run_stock_ai(symbol, exchange, title, filename):
    """Run the stock_ai.py script with the given parameters using the virtual environment's Python interpreter."""
    python_executable = get_virtual_env_python()
    subprocess.Popen([python_executable, 'stock_ai.py', symbol, exchange, title, filename])

def load_targets_and_run():
    """Load targets from CSV and run the stock_ai.py script for each."""
    with open(os.path.join('config', 'targets.csv'), mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            symbol = row['Symbol']
            exchange = row['Exchange']
            title = row['Title']
            filename = row['Filename']
            print(f"Running stock_ai.py for {symbol} on {exchange}...")
            run_stock_ai(symbol, exchange, title, filename)

def combine_signal_files():
    """Combine all signal system files into a single data/result.csv with a PAIR column first and sorted by Buy Time."""
    target_file = os.path.join('data', 'result.csv')
    all_data = []

    # Load targets from CSV
    with open(os.path.join('config', 'targets.csv'), mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row['Title']
            filename = row['Filename']
            
            signal_system_file = os.path.join('data', f"{filename}_Signal_System.csv")
            
            if os.path.exists(signal_system_file):
                # Read each signal system file and add the "PAIR" column
                data = pd.read_csv(signal_system_file)
                data['PAIR'] = f"{title}"
                all_data.append(data)
            else:
                print(f"Warning: {signal_system_file} does not exist.")

    if all_data:
        # Combine all data into a single DataFrame
        combined_data = pd.concat(all_data, ignore_index=True)

        # Reorder columns to have "PAIR" first
        columns = ['PAIR', 'Buy Time', 'Buy Price', 'Take Profit', 'Stop Loss', 'Close', 'Close Time', '%']
        combined_data = combined_data[columns]

        # Sort by "Buy Time"
        combined_data.sort_values(by=['Buy Time'], inplace=True)

        # Save to data/result.csv
        combined_data.to_csv(target_file, index=False)
        print(f"Combined result saved to {target_file}.")
    else:
        print("No data to combine.")

if __name__ == '__main__':
    combine_signal_files()
    load_targets_and_run()

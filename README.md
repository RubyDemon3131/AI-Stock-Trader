
# **AI Stock Trader**

## **Table of Contents**
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Adding Symbols and Exchanges](#adding-symbols-and-exchanges)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## **Introduction**

Welcome to **AI Stock Trader**, a powerful tool designed to fetch real-time stock market data, calculate key technical indicators using AI-powered strategies, and generate trading signals. This project enables continuous data analysis and backtesting, making it an essential tool for modern traders.

---

## **Features**

- **AI-Powered Trading Strategies:** Implement customizable AI-driven trading strategies.
- **Real-Time Data Fetching:** Fetch OHLCV data from TradingView at regular intervals.
- **Technical Indicator Calculation:** Automatically compute RSI, MACD, and StochRSI indicators.
- **Signal Generation:** Generate buy and sell signals based on defined AI strategies.
- **Robust Error Handling:** Gracefully handle data fetch errors and retries.

---

## **Installation**

### **Prerequisites**

- Python 3.7 or higher
- `pip` package manager
- TradingView account (optional)

### **Clone the Repository**

```bash
git clone https://github.com/yourusername/ai-stock-trader.git
cd ai-stock-trader
```

### **Install Required Packages**

```bash
pip install -r requirements.txt
```

### **Setup Configuration**

Edit the `config/strategy_config.json` file to customize your AI-driven trading strategy parameters.

---

## **Usage**

### **Starting the Data Fetcher**

Run the data fetcher to continuously update your data and generate signals:

```python
from data_fetcher import start_data_fetching

start_data_fetching(chart, 'data/ohlcv.csv', 'data/signals.csv', 'BTCUSD', 'Binance', 'config/strategy_config.json')
```

---

## **Configuration**

### **Strategy Configuration**
The `config/strategy_config.json` file allows you to define the parameters for your AI trading strategy, including:

- **Take Profit**: Percentage at which to take profit.
- **Stop Loss**: Percentage at which to stop loss.
- **RSI Period**: Number of periods for RSI calculation.
- **MACD Parameters**: Fast, slow, and signal periods for MACD calculation.
- **StochRSI Period**: Period for StochRSI calculation.
- **Overbought/Oversold Levels**: Thresholds for RSI and StochRSI.

---

## **Adding Symbols and Exchanges**

You can add symbols and exchanges to track by editing the `config/targets.csv` file. This allows you to customize the stocks or other financial instruments you want to monitor.

### **Symbol and Exchange List**

A comprehensive list of symbols and exchanges can be found at [TradingView Database](https://tvdb.brianthe.dev/). Use this resource to find the correct identifiers for the symbols and exchanges you wish to track.

---

## **Project Structure**

```plaintext
├── data_fetcher.py           # Main script for fetching and updating data
├── trading_strategy.py       # Handles indicator calculations and signal generation
├── indicators/               # Custom indicator implementations (RSI, MACD, StochRSI)
├── utils/                    # Utility functions (file handling, signal processing)
├── data/                     # Directory for storing OHLCV and signal data
├── config/                   # Configuration files (strategy_config.json, targets.csv)
├── requirements.txt          # Required Python packages
└── README.md                 # Project documentation
```

---

## **Contributing**

We welcome contributions to enhance the functionality of AI Stock Trader. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
## **Contact**

For any questions or inquiries, please contact:

- **Christopher Bulat**: [rubydemon3131@gmail.com](mailto:ianharding@example.com)
Dummy change number 1

Dummy change number 1

Dummy change number 6 at Thu Sep 19 18:36:01 EDT 2024
Dummy change number 7 at Thu Sep 19 18:36:20 EDT 2024
Dummy change number 8 at Thu Sep 19 18:36:39 EDT 2024
Dummy change number 9 at Thu Sep 19 18:36:57 EDT 2024
Dummy change number 10 at Thu Sep 19 18:37:17 EDT 2024
Dummy change number 11 at Thu Sep 19 18:37:38 EDT 2024
Dummy change number 12 at Thu Sep 19 18:37:59 EDT 2024
Dummy change number 13 at Thu Sep 19 18:38:19 EDT 2024
Dummy change number 14 at Thu Sep 19 18:38:39 EDT 2024
Dummy change number 15 at Thu Sep 19 18:39:00 EDT 2024
Dummy change number 16 at Thu Sep 19 18:39:20 EDT 2024
Dummy change number 17 at Thu Sep 19 18:39:41 EDT 2024
Dummy change number 18 at Thu Sep 19 18:40:01 EDT 2024
Dummy change number 19 at Thu Sep 19 18:40:21 EDT 2024
Dummy change number 20 at Thu Sep 19 18:40:41 EDT 2024
Dummy change number 21 at Thu Sep 19 18:41:02 EDT 2024
Dummy change number 22 at Thu Sep 19 18:41:22 EDT 2024
Dummy change number 23 at Thu Sep 19 18:41:42 EDT 2024
Dummy change number 24 at Thu Sep 19 18:42:03 EDT 2024
Dummy change number 25 at Thu Sep 19 18:42:23 EDT 2024
Dummy change number 26 at Thu Sep 19 18:42:45 EDT 2024
Dummy change number 27 at Thu Sep 19 18:43:05 EDT 2024
Dummy change number 28 at Thu Sep 19 18:43:25 EDT 2024
Dummy change number 29 at Thu Sep 19 18:43:45 EDT 2024
Dummy change number 30 at Thu Sep 19 18:44:05 EDT 2024
Dummy change number 31 at Thu Sep 19 18:44:26 EDT 2024
Dummy change number 32 at Thu Sep 19 18:44:46 EDT 2024
Dummy change number 33 at Thu Sep 19 18:45:07 EDT 2024
Dummy change number 34 at Thu Sep 19 18:45:27 EDT 2024
Dummy change number 35 at Thu Sep 19 18:45:48 EDT 2024
Dummy change number 36 at Thu Sep 19 18:46:08 EDT 2024
Dummy change number 37 at Thu Sep 19 18:46:27 EDT 2024
Dummy change number 38 at Thu Sep 19 18:46:46 EDT 2024
Dummy change number 39 at Thu Sep 19 18:47:06 EDT 2024
Dummy change number 40 at Thu Sep 19 18:47:26 EDT 2024
Dummy change number 41 at Thu Sep 19 18:47:48 EDT 2024
Dummy change number 42 at Thu Sep 19 18:48:09 EDT 2024
Dummy change number 43 at Thu Sep 19 18:48:29 EDT 2024
Dummy change number 44 at Thu Sep 19 18:48:49 EDT 2024
Dummy change number 45 at Thu Sep 19 18:49:10 EDT 2024
Dummy change number 46 at Thu Sep 19 18:49:30 EDT 2024
Dummy change number 47 at Thu Sep 19 18:49:50 EDT 2024
Dummy change number 48 at Thu Sep 19 18:50:10 EDT 2024
Dummy change number 49 at Thu Sep 19 18:50:33 EDT 2024
Dummy change number 50 at Thu Sep 19 18:50:53 EDT 2024
Dummy change number 51 at Thu Sep 19 18:51:13 EDT 2024
Dummy change number 52 at Thu Sep 19 18:51:33 EDT 2024
Dummy change number 53 at Thu Sep 19 18:51:53 EDT 2024
Dummy change number 54 at Thu Sep 19 18:52:13 EDT 2024
Dummy change number 55 at Thu Sep 19 18:52:33 EDT 2024
Dummy change number 56 at Thu Sep 19 18:52:54 EDT 2024
Dummy change number 57 at Thu Sep 19 18:53:15 EDT 2024


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
Dummy change number 58 at Thu Sep 19 18:53:35 EDT 2024
Dummy change number 59 at Thu Sep 19 18:53:56 EDT 2024
Dummy change number 60 at Thu Sep 19 18:54:16 EDT 2024
Dummy change number 61 at Thu Sep 19 18:54:37 EDT 2024
Dummy change number 62 at Thu Sep 19 18:54:57 EDT 2024
Dummy change number 63 at Thu Sep 19 18:55:17 EDT 2024
Dummy change number 64 at Thu Sep 19 18:56:04 EDT 2024
Dummy change number 65 at Thu Sep 19 18:56:25 EDT 2024
Dummy change number 66 at Thu Sep 19 18:56:45 EDT 2024
Dummy change number 67 at Thu Sep 19 18:57:06 EDT 2024
Dummy change number 68 at Thu Sep 19 18:57:26 EDT 2024
Dummy change number 69 at Thu Sep 19 18:57:47 EDT 2024
Dummy change number 70 at Thu Sep 19 18:58:08 EDT 2024
Dummy change number 71 at Thu Sep 19 18:58:30 EDT 2024
Dummy change number 72 at Thu Sep 19 18:58:50 EDT 2024
Dummy change number 73 at Thu Sep 19 18:59:11 EDT 2024
Dummy change number 74 at Thu Sep 19 18:59:33 EDT 2024
Dummy change number 75 at Thu Sep 19 18:59:54 EDT 2024
Dummy change number 76 at Thu Sep 19 19:00:14 EDT 2024
Dummy change number 77 at Thu Sep 19 19:00:34 EDT 2024
Dummy change number 78 at Thu Sep 19 19:00:54 EDT 2024
Dummy change number 79 at Thu Sep 19 19:01:14 EDT 2024
Dummy change number 80 at Thu Sep 19 19:01:34 EDT 2024
Dummy change number 81 at Thu Sep 19 19:01:55 EDT 2024
Dummy change number 82 at Thu Sep 19 19:02:16 EDT 2024
Dummy change number 83 at Thu Sep 19 19:02:37 EDT 2024
Dummy change number 84 at Thu Sep 19 19:02:57 EDT 2024
Dummy change number 85 at Thu Sep 19 19:03:17 EDT 2024
Dummy change number 86 at Thu Sep 19 19:03:37 EDT 2024
Dummy change number 87 at Thu Sep 19 19:03:58 EDT 2024
Dummy change number 88 at Thu Sep 19 19:04:18 EDT 2024
Dummy change number 89 at Thu Sep 19 19:04:38 EDT 2024
Dummy change number 90 at Thu Sep 19 19:04:59 EDT 2024
Dummy change number 91 at Thu Sep 19 19:05:20 EDT 2024
Dummy change number 92 at Thu Sep 19 19:05:40 EDT 2024
Dummy change number 93 at Thu Sep 19 19:06:00 EDT 2024
Dummy change number 94 at Thu Sep 19 19:06:21 EDT 2024
Dummy change number 95 at Thu Sep 19 19:06:42 EDT 2024
Dummy change number 96 at Thu Sep 19 19:07:04 EDT 2024
Dummy change number 97 at Thu Sep 19 19:07:26 EDT 2024
Dummy change number 98 at Thu Sep 19 19:07:47 EDT 2024
Dummy change number 99 at Thu Sep 19 19:08:11 EDT 2024
Dummy change number 100 at Thu Sep 19 19:08:34 EDT 2024
Dummy change number 101 at Thu Sep 19 19:08:56 EDT 2024
Dummy change number 102 at Thu Sep 19 19:09:19 EDT 2024
Dummy change number 103 at Thu Sep 19 19:09:43 EDT 2024
Dummy change number 104 at Thu Sep 19 19:10:04 EDT 2024
Dummy change number 105 at Thu Sep 19 19:10:26 EDT 2024
Dummy change number 106 at Thu Sep 19 19:10:49 EDT 2024
Dummy change number 107 at Thu Sep 19 19:11:10 EDT 2024
Dummy change number 108 at Thu Sep 19 19:11:31 EDT 2024
Dummy change number 109 at Thu Sep 19 19:11:52 EDT 2024
Dummy change number 110 at Thu Sep 19 19:12:13 EDT 2024
Dummy change number 111 at Thu Sep 19 19:12:34 EDT 2024
Dummy change number 112 at Thu Sep 19 19:12:57 EDT 2024
Dummy change number 113 at Thu Sep 19 19:13:22 EDT 2024
Dummy change number 114 at Thu Sep 19 19:13:43 EDT 2024
Dummy change number 115 at Thu Sep 19 19:14:05 EDT 2024
Dummy change number 116 at Thu Sep 19 19:14:26 EDT 2024
Dummy change number 117 at Thu Sep 19 19:14:47 EDT 2024
Dummy change number 118 at Thu Sep 19 19:15:08 EDT 2024
Dummy change number 119 at Thu Sep 19 19:15:29 EDT 2024
Dummy change number 120 at Thu Sep 19 19:15:50 EDT 2024
Dummy change number 121 at Thu Sep 19 19:16:13 EDT 2024
Dummy change number 122 at Thu Sep 19 19:16:35 EDT 2024
Dummy change number 123 at Thu Sep 19 19:16:57 EDT 2024
Dummy change number 124 at Thu Sep 19 19:17:18 EDT 2024
Dummy change number 125 at Thu Sep 19 19:17:41 EDT 2024
Dummy change number 126 at Thu Sep 19 19:18:04 EDT 2024
Dummy change number 127 at Thu Sep 19 19:18:25 EDT 2024
Dummy change number 128 at Thu Sep 19 19:18:48 EDT 2024
Dummy change number 129 at Thu Sep 19 19:19:09 EDT 2024
Dummy change number 130 at Thu Sep 19 19:19:30 EDT 2024
Dummy change number 131 at Thu Sep 19 19:19:51 EDT 2024
Dummy change number 132 at Thu Sep 19 19:20:12 EDT 2024
Dummy change number 133 at Thu Sep 19 19:20:32 EDT 2024
Dummy change number 134 at Thu Sep 19 19:20:53 EDT 2024
Dummy change number 135 at Thu Sep 19 19:21:13 EDT 2024
Dummy change number 136 at Thu Sep 19 19:21:33 EDT 2024
Dummy change number 137 at Thu Sep 19 19:21:54 EDT 2024
Dummy change number 138 at Thu Sep 19 19:22:14 EDT 2024
Dummy change number 139 at Thu Sep 19 19:22:35 EDT 2024

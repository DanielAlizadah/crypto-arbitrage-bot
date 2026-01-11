# Real-Time Crypto currency Arbitrage System

A  price discrepancy scanner written using Python.This system/tool monitors the Bid and Ask of major cryptocurrency exchanges to identify arbitrage opportunities in real-time. This particular code is focussed on Bitcoin, however that can easily be changed. 

## 🚀 Project Overview
This project was developed to demonstrate the application of automated data collection and financial logic in a live market environment. Unlike basic "price trackers," this scanner accounts for the **Bid/Ask spread**, ensuring that detected opportunities are tradeable rather than theoretical.

### Key Features
* **Live Data:** Updates Data of Binance and Kraken using the CCXT library.
* **Bid/Ask Logic:** Calculates profitability based on the lowest selling price (Ask) and highest buying price (Bid) across exchanges in this particular case of Bitcoin.
* **Automated Logging:** Saves all opportunities exceeding a 0.01% threshold to a Excel sheet.
* **Rate Limit:** Implementsrate limiting to ensure 24/7 operation without bans.

## 📈 Methodology
The bot follows strict logic to identify market arbitrage:
1.  **Fetch:** Concurrent requests for order book tickers.
2.  **Verify:** Checks for data integrity (null values/missing bids).
3.  **Calculate:** * `Spread A: ((Exchange_1_Bid - Exchange_2_Ask) / Exchange_2_Ask) * 100`
    * `Spread B: ((Exchange_2_Bid - Exchange_1_Ask) / Exchange_1_Ask) * 100`
4.  **Filter:** Only logs spreads that exceed the `min_profit_thresh` to account for exchange fees.

## 📊 How to Use
1.  **Install Dependencies:** `pip install ccxt`
2.  **Run Scanner:** `python bot.py`
3.  **Analyze Results:** View `arbitrage_log.csv` for time-stamped opportunities.

## 📂 Future Roadmap
* Add multi-currency scanning (ETH, SOL, etc.).
* Implement a real-time visualization dashboard using Matplotlib/Pandas.

## Image Graph Of Statistics
<img width="657" height="380" alt="image" src="https://github.com/user-attachments/assets/1de1811c-3e27-4475-9386-e59695cf5009" />

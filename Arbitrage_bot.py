import os
import ccxt # type: ignore
import time
import datetime
import csv

class Arbitrage_System:
    def __init__(self, symbol):
        self.ex1 = ccxt.binance({'enableRateLimit': True})
        self.ex2 = ccxt.kraken({'enableRateLimit': True})
        self.symbol = symbol
        self.filename = "arbitrage_log.csv"
        self.init_csv()

    def init_csv(self):
        # Check if file exists. If not, create it with headers.
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as f:
                writer = csv.writer(f)
                # These are your Excel Column Headers
                writer.writerow(["Time", "Symbol", "Direction", "Spread (%)"])
            print(f"Created new file: {self.filename}")
            
    def get_prices(self):
        try:
            price1 = self.ex1.fetch_ticker(self.symbol)
            price2 = self.ex2.fetch_ticker(self.symbol)

            return price1, price2
        except Exception as e:
            print("Hmm, something went wrong")
            return None, None

    def log_to_csv(self, direction, spread):
        try:
            with open(self.filename, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([time.ctime(), self.symbol, direction, f"{spread:.4f}%"])
        except PermissionError:
            print("\n[ERROR] Could not log to CSV! Close the Excel file to fix this.")

    def run(self):
        print(f"Scanning {self.symbol}... Press Ctrl+C to stop.")
        while True:
            price1, price2 = self.get_prices()
            min_profit_thresh = 0.009
            if price1 and price2:

                bin_bid = price1["bid"]
                bin_ask = price1["ask"]

                krak_bid = price2["bid"]
                krak_ask = price2["ask"]

                if bin_bid and bin_ask and krak_bid and krak_ask :
                    spread1 = ((bin_bid - krak_ask) / krak_ask) * 100
                    spread2 = ((krak_bid - bin_ask)/ bin_ask) * 100

                    if spread1 > min_profit_thresh:
                        print(f"BUY Kraken, SELL Binance. Profit: {spread1:.2f}% (logging to CSV)")
                        self.log_to_csv("Kraken -> Binance",spread1)
                    elif spread2 > min_profit_thresh:
                        print(f"BUY Binance, SELL Kraken. Profit: {spread2:.2f}% (logging to CSV)")
                        self.log_to_csv("Binance -> Kraken",spread2)
                    else:
                        # Print a 'heartbeat' so you know it's working
                        current_max = max(spread1, spread2)
                        now = datetime.datetime.now().strftime("%H:%M:%S")
                        print(f"[{now}] Scanning... Best spread: {current_max:.2f}% ", end="\r", flush=True)
            time.sleep(2)

if __name__ == "__main__":
    # Create the object for BTC
    bot = Arbitrage_System("BTC/USDT")
    
    # Start the infinite loop
    bot.run()


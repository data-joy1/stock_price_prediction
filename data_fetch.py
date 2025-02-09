import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start="2020-01-01", end="2024-01-01"):
    stock = yf.download(ticker, start=start, end=end)
    stock.reset_index(inplace=True)
    return stock

if __name__ == "__main__":
    df = fetch_stock_data("AAPL")  # Fetch Apple stock data
    print(df.head())

import pandas as pd
import yfinance as yf
from pathlib import Path

class DataLoader: 
    def __init__(self, data_dir='data/raw'):
        """Gets the path for raw data
        Args: data_dir: data directory for raw data"""
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def load_large_csv(self, filepath, chunksize=10000):
        """Generator to load large CSV files in chunks. Saves memory when loading large datasets"""
        for chunk in pd.read_csv(filepath, chunksize=chunksize):
            yield chunk

    def load_commodity_prices(self, ticker, start_date, end_date):
        """Load commodity price data from Yahoo Finance API
        Args: 
        self: 
        ticker: 
        start_date: Start Date for data
        end_date: End Date for data"""
        data = yf.download(ticker, start = start_date, end = end_date)
        output_path = self.data_dir / f"{ticker}_prices.csv"
        data.to_csv(output_path)
        n_commodities = len(data)
        print(f"Saved {n_commodities} rows of commodity data to {output_path}. ")
        yield data
    
    def load_trade_data(self, filepath):
        """Load UN Comtrade or World Bank trade data"""
        df = pd.read_csv(filepath)
        print(f"Loaded {len(df)} trade records")
        yield df

    def load_news_data(self, filepath):
        """Load news/GDELT data for entity extraction"""
        df = pd.read_csv(filepath)
        print(f"Loaded {len(df)} news article")
        yield df

if __name__ == "main":
    loader = DataLoader()

    for trade_data_chunk in loader.load_trade_data('data/raw/comtrade_large_data.csv'):
        print(f"Loaded chunk with shape: {trade_data_chunk}")

    # Load gold commodity prices
    for gold_data in loader.load_commodity_prices('GC=F', '2023-01-01', '2024-01-01'):
        print (gold_data.head())
    # Load trade data (once you download from UN Comtrade)
    # trade_data = loader.load_trade_data('data/raw/comtrade_electronics.csv')
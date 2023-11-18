import yfinance as yf
import pandas as pd 
from datetime import datetime

# Define the stock symbol and time range
stock_symbol = "RELIANCE.NS"
start_date = "1996-01-01"
end_date = datetime.today().strftime('%Y-%m-%d')  # Current date

# Fetch stock data using yfinance
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Display the stock data
#print(stock_data.head())
stock_data.to_csv('RELIANCE.csv')
# precise_stock_price.py
import yfinance as yf
from datetime import datetime, timedelta
import os
import sys
import pandas as pd

stock = "AMZN"
month = 11
year = 2023

price_data = {}

for date in range(1, 31):
    last_date = (datetime(year, (month % 12) + 1, 1) - timedelta(days=1)).day
    main_date = min(date, last_date)
    startd = f"{year}-{month:02d}-01"
    endd = f"{year}-{month:02d}-{last_date:02d}"
    target = datetime(year, month, main_date)
    data = yf.download(stock, startd, endd)
    try:
        price = data.loc[target.strftime("%Y-%m-%d")]["Low"]
        price_data[target] = round(price, 2)
    except KeyError:
        print(f"No data available for {target.strftime('%Y-%m-%d')}")
    except Exception as e:
        print(f"Exception Error: {e}")

# Save historical stock prices to a CSV file
historical_data = pd.DataFrame(price_data.items(), columns=['Date', 'Low Price'])
historical_data.to_csv('historical_stock_prices.csv', index=False)

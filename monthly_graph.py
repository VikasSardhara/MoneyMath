# monthly_graph.py
import calendar
import yfinance as yf
from datetime import datetime, timedelta
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

print("This program will give you stock prices for each day of the month")
print("    ")
print("    ")
print("\033[95mTo run this file, use the following command:\033[0m")
print("\033[92mpython precise_stock_price.py <stock_symbol> <month> <year>\033[0m")
print("    ")
print("    ")

price_data = {}
stock = input("Enter Stock Symbol: ").upper()
month = int(input("Enter number of month: "))
year = int(input("Enter year: "))

for date in range(1, calendar.monthrange(year, month)[1] + 1):
    last_date = calendar.monthrange(year, month)[1]
    main_date = min(date, last_date)
    startd = f"{year}-{month:02d}-01"
    endd = f"{year}-{month:02d}-{last_date:02d}"
    target = datetime(year, month, main_date)
    data = yf.download(stock, startd, endd)
    try:
        price = data.loc[target.strftime("%Y-%m-%d")]["Low"]
        price_data[date] = round(price, 2)
        os.system("cls")
    except KeyError:
        print(f"No data available for {target.strftime('%Y-%m-%d')}")
    except Exception as e:
        print(f"Exception Error: {e}")

print(" ")

company_name = yf.Ticker(stock).info.get("longName", "Company Name Not Found")
print(f"The company {company_name} ({stock}) is performing in {month}-{year}: ")
print(" ")
print("\033[94mGiven data is about the lowest price on that particular day\033[0m")
print(" ")

# Plotting the graph
dates = [datetime(year, month, date) for date in price_data.keys()]
prices = list(price_data.values())

plt.plot(dates, prices, label="Stock Prices", marker='o', linestyle='-', color='b')
plt.title(f"Stock Prices for {company_name} ({stock}) in {calendar.month_name[month]}-{year}")
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.legend()
plt.show()

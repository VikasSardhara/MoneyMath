import yfinance as yf
from datetime import datetime, timedelta
import os

price_data = {}
print("This program will give you stock price for each day of the year")

print("    ")
print("    ")
print("\033[95mTo run this file, use the following command:\033[0m")
print("\033[92mRun this file: python precise_stock_price.py <stock_symbol> <year>\033[0m")
print("    ")
print("    ")

stock = input("Enter Stock Symbol: ").upper()
year = int(input("Enter year: "))


for month in range(1, 13):
    for date in range(1, 32):
        last_date = (datetime(year, (month % 12) + 1, 1) - timedelta(days=1)).day
        main_date = min(date, last_date)
        startd = f"{year}-{month:02d}-01"
        endd = f"{year}-{month:02d}-{last_date:02d}"
        target = datetime(year, month, main_date)
        data = yf.download(stock, startd, endd)
        try:
            price = data.loc[target.strftime("%Y-%m-%d")]["Low"]
            price_data[target] = round(price, 2)
            os.system("cls")
        except KeyError:
            print(f"No data available for {target.strftime('%Y-%m-%d')}")
        except Exception as e:
            print(f"Exception Error: {e}")

os.system('cls')

company_name = yf.Ticker(stock).info.get("longName", "Company Name Not Found")
print(f"The company {company_name} ({stock}) is performing in {year}: ")
print(" ")
print("\033[94mGiven data is about Lowest price on that particular day\033[0m")
print(" ")

for date, price in price_data.items():
    formatted_date = date.strftime("%d-%m-%Y")
    print(f"{formatted_date} : {price}")
print(" ")

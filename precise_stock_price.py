import yfinance as yf
from datetime import datetime, timedelta
import os
import sys

print("This programm will give you stock price of each day of month")

print("    ")
print("    ")
print("\033[95mTo run this file, use the following command:\033[0m")
print("\033[92mFor Fedex: python precise_stock_price.py FDX 11 2023\033[0m")
print("    ")
print("    ")

price_data = {}
stock = sys.argv[1].upper()
month = int(sys.argv[2])
year = int(sys.argv[3])

for date in range(1,31):   
    last_date = (datetime(year, (month % 12) + 1, 1) - timedelta(days=1)).day  
    main_date = min (date, last_date)
    startd = f"{year}-{month}-01"
    endd = f"{year}-{month}-{last_date}"
    target = datetime(year, month, main_date)   
    data = yf.download(stock, startd, endd)
    try:
        price = data.loc[target.strftime("%Y-%m-%d")]["Low"]
        price_data[date] = round(price, 2)
    except KeyError:
         print(f"No data available for {target.strftime('%Y-%m-%d')}")
    except Exception as e:
        print(f"Exception Error: {e}")

os.system('cls')

company_name = yf.Ticker(stock).info.get("longName", "Company Name Not Found")
print(f"The company {company_name} ({stock}) is performing in {month}-{year}: ")
print(" ")
print("\033[94mGiven data is about Lowest price on that particular day\033[0m")
print(" ")

for date, price in price_data.items():
    formatted_date = datetime(year, month, date).strftime("%d-%m-%Y")

    print(f"{formatted_date} : {price}")
print(" ")

    
    

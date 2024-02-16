import yfinance as yf
from datetime import datetime, timedelta
import os

print("This programm will give you stock price of each day of month")

price_data = {}

stock = input("Enter Stock Symbol in Uppercase: ")
month = int(input("Enter number of month: "))
year = int(input("Enter year: "))

for date in range(1,31):
    last_date = (datetime(year, (month % 12) + 1, 1) - timedelta(days=1)).day
    main_date = min (date, last_date)

    startd = f"{year}-{month}-01"
    endd = f"{year}-{month}-{last_date}"

    target = datetime(year, month, main_date)   
    
    
    data = yf.download(stock, startd, endd)
    try:
        price = data.loc[target.strftime("%Y-%m-%d")]["Close"]
        price_data[date] = round(price, 2)
    except KeyError:
        print(f"No data available for {target.strftime('%Y-%m-%d')}")
    except Exception as e:
        print(f"Exception Error: {e}")

os.system('cls')

for date, price in price_data.items():
    formatted_date = datetime(year, month, date).strftime("%d-%m-%Y")
    print(f"{formatted_date} : {price}")


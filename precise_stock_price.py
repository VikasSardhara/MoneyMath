import yfinance as yf
from datetime import datetime, timedelta

date = int(input("Enter date: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
stock = "AMZN"

last_day = (datetime(year, (month % 12)+1, 1) - timedelta(days=1)).day
day = min (date, last_day)

startd = f"{year}-{month}-01"
endd = f"{year}-{month}-{last_day}"
data = yf.download(stock, startd, endd)

try:
    tdate = datetime(year, month, day)
    price = data.loc[tdate.strftime("%Y-%m-%d")]["Close"]
    print(price)

except KeyError:
    print("Keyerror")

except Exception as e:
    print(f"Error{e}")
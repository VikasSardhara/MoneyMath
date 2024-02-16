# process_data.py
import yfinance as yf
from datetime import datetime, timedelta
import os

def process_stock_data(stock, month, year):
    price_data = {}
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

    return price_data

def save_to_file(stock, month, year, price_data):
    with open('output.txt', 'w') as file:
        for date, price in price_data.items():
            formatted_date = datetime(year, month, date).strftime("%d-%m-%Y")
            file.write(f"{formatted_date} : {str(price)}\n")

if __name__ == "__main__":
    stock = input("Enter Stock Symbol in Uppercase: ")
    month = int(input("Enter number of month: "))
    year = int(input("Enter year: "))
    
    price_data = process_stock_data(stock, month, year)
    save_to_file(stock, month, year, price_data)

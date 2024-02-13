import yfinance as yf
from datetime import datetime, timedelta

def process(date, month, year, stock_symbol):
    last_date = (datetime(year, (month % 12) + 1, 1) - timedelta(days=1)).day
    day = min(date, last_date)
    start_date = f"{year}-{month:02d}-01"
    end_date = f"{year}-{month:02d}-{last_date}"
    
    try:
        target_date = datetime(year, month, day)
        data = yf.download(stock_symbol, start_date, end_date)
        price = data.loc[target_date.strftime("%Y-%m-%d")]["Close"]
        print(f"Closing price on {target_date.strftime('%Y-%m-%d')}: {price}")
    except KeyError:
        print("Error: Data not available for the specified date.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    date_input = int(input("Enter date: "))
    month_input = int(input("Enter month: "))
    year_input = int(input("Enter year: "))
    stock_input = str(input("Enter Stock Symbol: "))

    process(date_input, month_input, year_input, stock_input)

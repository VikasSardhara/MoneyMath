import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def get_previous_weekday(date):
    while date.weekday() > 4:  # Monday to Friday are considered weekdays (0 to 4)
        date -= timedelta(days=1)
    return date

def get_target_date_prices(stock_symbol, start_year, end_year):
    target_month = int(input("Enter the target month (1-12): "))
    target_day = int(input("Enter the target day of the month: "))

    prices = []

    for year in range(start_year, end_year + 1):
        try:
            target_date = datetime(year, target_month, target_day)
            if target_date.weekday() > 4:  # If the target date is Saturday or Sunday, get the previous Friday's date
                target_date = get_previous_weekday(target_date)

            # Fetch historical stock data from Yahoo Finance
            stock_data = yf.download(stock_symbol, start=f'{year}-{target_month:02d}-01', end=f'{year}-{target_month:02d}-31', progress=False)

            # Find the closing price for the target date or the previous trading day
            closing_price = stock_data.loc[target_date.strftime('%Y-%m-%d')]['Close']
            prices.append({'Year': year, 'Closing Price': closing_price})

        except Exception as e:
            print(f"Error processing {stock_symbol} for {year}: {e}")

    return prices

def main():
    stock_symbol = 'FDX'
    start_year = 2015
    end_year = 2023

    result = get_target_date_prices(stock_symbol, start_year, end_year)

    print(f"Closing prices for {stock_symbol} on the specified target date:")
    for entry in result:
        print(f"x = {entry['Year']}, y = ${entry['Closing Price']:.2f}")

if __name__ == "__main__":
    main()

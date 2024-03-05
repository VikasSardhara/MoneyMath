import yfinance as yf
from datetime import datetime, timedelta
import calendar
import matplotlib.pyplot as plt
import os

def process_stock_data(stock, year, month):
    """Process stock data and return the highest and lowest prices and dates for the month."""
    highest_price = 0  # Initialize to 0
    lowest_price = float('inf')  # Initialize to positive infinity
    highest_price_date = None
    lowest_price_date = None
    for date in range(1, 32):
        last_date = (datetime(year, (month % 12) + 1, 1) - timedelta(days=1)).day
        main_date = min(date, last_date)
        startd = f"{year}-{month:02d}-01"
        endd = f"{year}-{month:02d}-{last_date:02d}"
        target = datetime(year, month, main_date)
        data = yf.download(stock, startd, endd)
        try:
            high_price = data.loc[target.strftime("%Y-%m-%d")]["High"]
            low_price = data.loc[target.strftime("%Y-%m-%d")]["Low"]
            if high_price > highest_price:
                highest_price = round(high_price, 2)
                highest_price_date = target.strftime("%Y-%m-%d")
                
            if low_price < lowest_price:
                lowest_price = round(low_price, 2)
                lowest_price_date = target.strftime("%Y-%m-%d")
                
            os.system('cls')
        except KeyError:
            print(f"No data available for {target.strftime('%Y-%m-%d')}")
        except Exception as e:
            print(f"Exception Error: {e}")
    return highest_price, highest_price_date, lowest_price, lowest_price_date

def plot_prices_comparison(stock, year, prices_dict):
    """Plot the highest and lowest prices for each month on the same graph."""
    months = list(prices_dict.keys())
    highest_prices = [values["Highest Price"] for values in prices_dict.values()]
    lowest_prices = [values["Lowest Price"] for values in prices_dict.values()]
    highest_price_dates = [values["Highest Date"] for values in prices_dict.values()]
    lowest_price_dates = [values["Lowest Date"] for values in prices_dict.values()]

    # Line Graph
    plt.figure(figsize=(12, 6))
    plt.plot(months, highest_prices, marker='o', label='Highest Prices', color='green', linestyle='-', linewidth=2)
    plt.plot(months, lowest_prices, marker='o', label='Lowest Prices', color='blue', linestyle='-', linewidth=2)

    # Annotate points with date information
    for i, date in enumerate(highest_price_dates):
        plt.annotate(f'\n{date}', (months[i], highest_prices[i]), textcoords="offset points", xytext=(0,10), ha='center')

    for i, date in enumerate(lowest_price_dates):
        plt.annotate(f'\n{date}', (months[i], lowest_prices[i]), textcoords="offset points", xytext=(0,10), ha='center')

    plt.title(f"Highest and Lowest Stock Prices for {stock} in {year}")
    plt.xlabel("Month")
    plt.ylabel("Price")
    plt.grid(axis='y')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    stock = input("Enter Stock Symbol: ").upper()
    year = int(input("Enter year: "))

    # Create a dictionary to store the highest and lowest prices and dates for each month
    prices_dict = {}

    # Process and store the highest and lowest prices and dates for each month
    for month in range(1, 13):
        highest_price, highest_price_date, lowest_price, lowest_price_date = process_stock_data(stock, year, month)
        prices_dict[f"Month {month:02d}"] = {
            "Highest Price": highest_price,
            "Highest Date": highest_price_date,
            "Lowest Price": lowest_price,
            "Lowest Date": lowest_price_date
        }

    # Print the dictionary at the end
    print("\nStock Prices Comparison for each month:")
    for month, values in prices_dict.items():
        print(f"{month} : Highest Price = {values['Highest Price']} on {values['Highest Date']}, Lowest Price = {values['Lowest Price']} on {values['Lowest Date']}")

    # Plot the highest and lowest prices for each month on the same graph
    plot_prices_comparison(stock, year, prices_dict)

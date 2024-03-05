# stock_graph_of_each_month.py
import yfinance as yf
from datetime import datetime, timedelta
import os
import sys
import matplotlib
matplotlib.use('Agg')  # Use Agg backend which doesn't require an interactive environment
import matplotlib.pyplot as plt

def process_stock_data(stock, year, month):
    """Process stock data and return a dictionary of date: low price."""
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
    return price_data

def save_to_file(stock, year, month, price_data, folder_path):
    """Save processed data to a file."""
    with open(os.path.join(folder_path, f'output_{month}.txt'), 'w') as file:
        for date, price in price_data.items():
            formatted_date = date.strftime("%d-%m-%Y")
            file.write(f"{formatted_date} : {str(price)}\n")

def plot_graph(stock, year, month, price_data, folder_path):
    """Generate and save a graph for the given month."""
    dates = list(price_data.keys())
    prices = list(price_data.values())

    plt.figure(figsize=(10, 6))
    plt.plot(dates, prices, marker='o', linestyle='-', color='b')
    plt.title(f"Stock Prices for {stock} in {month:02d}-{year}")
    plt.xlabel("Date")
    plt.ylabel("Low Price")
    plt.grid(True)
    plt.savefig(os.path.join(folder_path, f'{stock}_graph_of{month}_of_{year}.png'))
    plt.close()

if __name__ == "__main__":
    stock = input("Enter Stock Symbol: ").upper()
    year = int(input("Enter year: "))

    # Create a folder for images
    folder_path = f'{stock}_images_for_{year}'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Process and plot data for each month
    for month in range(1, 13):
        price_data = process_stock_data(stock, year, month)
        save_to_file(stock, year, month, price_data, folder_path)
        plot_graph(stock, year, month, price_data, folder_path)

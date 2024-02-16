# plot_graph.py
import matplotlib.pyplot as plt
from datetime import datetime

from process_data import process_stock_data

def plot_graph(stock, month, year):
    price_data = process_stock_data(stock, month, year)

    formatted_dates = [datetime(year, month, date) for date in price_data.keys()]
    prices = list(price_data.values())

    plt.plot(formatted_dates, prices, marker='o', linestyle='-', color='b')
    plt.title('Stock Prices')
    plt.xlabel('Date')
    plt.ylabel('Stock Price')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    stock = input("Enter Stock Symbol in Uppercase: ")
    month = int(input("Enter number of month: "))
    year = int(input("Enter year: "))

    plot_graph(stock, month, year)

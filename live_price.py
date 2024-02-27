import requests
import json
import time

def get_live_stock_price(api_key, stock_symbol):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_symbol}&apikey={api_key}'

    while True:
        try:
            response = requests.get(url)
            data = response.json()
            current_price = data["Global Quote"]["05. price"]
            print(f"Live Stock Price for {stock_symbol}: {current_price}")
        except Exception as e:
            print(f"Error fetching data: {e}")

        time.sleep(1)  # Refresh every 1 second

if __name__ == "__main__":
    api_key = "ICO7U0IDLYTJU3UK"
    stock_symbol = input("Enter the stock symbol: ").upper()
    get_live_stock_price(api_key, stock_symbol)

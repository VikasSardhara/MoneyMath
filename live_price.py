import yfinance as yf
import time

def get_live_stock_price(stock_symbols):
    while True:
        try:
            for symbol in stock_symbols:
                stock_data = yf.Ticker(symbol)
                current_price = stock_data.info.get("lastPrice")
                print(f"Live Stock Price for {symbol}: {current_price}")

        except Exception as e:
            print(f"Error fetching data: {e}")

        time.sleep(5)  # Refresh every 5 seconds

if __name__ == "__main__":
    stock_symbols = input("Enter comma-separated stock symbols (e.g., AAPL,GOOGL): ").upper().split(',')
    
    get_live_stock_price(stock_symbols)

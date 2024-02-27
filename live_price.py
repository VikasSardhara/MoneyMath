from yahoo_fin import stock_info
import time
import os 

def get_live_stock_prices(stock_symbols):
    while True:
        try:
            for symbol in stock_symbols:
                current_price = stock_info.get_live_price(symbol)
                os.system("cls")
                print(f"Live Stock Price for {symbol}: {current_price}")
                

        except Exception as e:
            print(f"Error fetching data: {e}")

        time.sleep(2)  # Refresh every 2 seconds

if __name__ == "__main__":
    stock_symbols = input("Enter comma-separated stock symbols (e.g., AMZN,GOOGL): ").upper().split(',')
    
    get_live_stock_prices(stock_symbols)

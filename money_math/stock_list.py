import yfinance as yf
import pandas as pd

def get_sp500_symbols():
    # Download the S&P 500 components from Wikipedia
    sp500_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    sp500_table = pd.read_html(sp500_url)[0]
    
    # Extract the stock symbols from the table
    sp500_symbols = sp500_table['Symbol'].tolist()
    
    return sp500_symbols

def save_symbols_to_file(symbols, file_name):
    with open(file_name, 'w') as file:
        for symbol in symbols:
            file.write(f"{symbol}\n")

# Example usage:
sp500_symbols = get_sp500_symbols()
save_symbols_to_file(sp500_symbols, 'sp500_symbols.txt')
print("S&P 500 Stock Symbols saved to sp500_symbols.txt")

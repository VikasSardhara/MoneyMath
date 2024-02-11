import yfinance as yf

def calculate_bvps_and_save(stock_symbol):
    try:
        # Download balance sheet data from Yahoo Finance
        balance_sheet = yf.Ticker(stock_symbol).balance_sheet

        if balance_sheet.empty:
            print("Balance sheet data is not available.")
            return None

        # Print column names in the balance sheet for debugging
        print("Column names in balance sheet:", balance_sheet.columns)

        # Update column names based on the actual names in your data
        total_assets_column = 'Total Assets'
        total_liabilities_column = 'Total Liab'
        preferred_stock_column = 'Preferred Stock'

        # Get the most recent total assets, total liabilities, and preferred stock
        total_assets = balance_sheet.iloc[0][total_assets_column]
        total_liabilities = balance_sheet.iloc[0][total_liabilities_column]
        preferred_stock = balance_sheet.iloc[0][preferred_stock_column]

        # ... rest of your code ...
        
        return bvps

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
calculate_bvps_and_save("AAPL")

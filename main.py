from precise_stock_price import get_stock_prices
from process_data import process_stock_data, save_to_file
from plot_graph import plot_graph
from stock_graph_of_each_month import generate_monthly_graphs
from lowprice_for_eachday import get_lowest_price

print("To Run this file: python main.py <Stock_sumbol> <year>")
def main():
    # Input for stock data processing
    stock = input("Enter Stock Symbol in Uppercase: ")
    month = int(input("Enter number of month: "))
    year = int(input("Enter year: "))
    
    # Get stock prices using precise_stock_price.py
    get_stock_prices(stock, month, year)

    # Process stock data
    price_data = process_stock_data(stock, month, year)

    # Save processed data to output.txt
    save_to_file(stock, month, year, price_data)
    
    # Plot the graph using the processed data
    plot_graph(stock, month, year)

    # Generate and save monthly graphs
    generate_monthly_graphs(stock, year)

    # Fetch and print the lowest price for each day of the year
    get_lowest_price(stock, year)

if __name__ == "__main__":
    main()

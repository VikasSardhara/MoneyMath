# main.py
from process_data import process_stock_data, save_to_file
from plot_graph import plot_graph

def main():
    # Input for stock data processing
    stock = input("Enter Stock Symbol in Uppercase: ")
    month = int(input("Enter number of month: "))
    year = int(input("Enter year: "))
    
    # Process stock data
    price_data = process_stock_data(stock, month, year)

    # Save processed data to output.txt
    save_to_file(stock, month, year, price_data)
    
    # Plot the graph using the processed data
    plot_graph(stock, month, year)

if __name__ == "__main__":
    main()

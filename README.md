# MoneyMath - Quantitative Finance Project

Welcome to MoneyMath, a Quantitative Finance project designed to analyze and visualize stock market data. Below is a brief overview of the project's components:

1. **plot_graph.py**
   - Description: This script generates a basic plot of stock prices for a given symbol and time range.
   - Usage: `python plot_graph.py <stock_symbol> <start_date> <end_date>`

2. **process_data.py**
   - Description: This module processes stock data, extracting relevant information for analysis.
   - Functions: `process_stock_data(stock, year, month)`, `save_to_file(stock, year, month, price_data, folder_path)`, `plot_graph(stock, year, month, price_data, folder_path)`

3. **main.py**
   - Description: The main script orchestrating the project, calling various modules to perform specific tasks.
   - Usage: `python main.py`

4. **precise_stock_price.py**
   - Description: Retrieves precise stock prices for a specific stock and time period, saving the data to a CSV file.
   - Usage: `python precise_stock_price.py <stock_symbol> <year>`

5. **stock_graph_of_each_month.py**
   - Description: Generates stock graphs for each month, showcasing low prices throughout the year.
   - Usage: `python stock_graph_of_each_month.py <stock_symbol> <year>`

6. **live_price.py**
   - Description: Continuously retrieves and displays live stock prices for specified stock symbols.
   - Usage: `python live_price.py`

7. **arima_forecast.py**
   - Description: Uses the ARIMA model to forecast future stock prices based on historical data.
   - Usage: `python arima_forecast.py`

8. **requirements.txt**
   - Description: Lists the required libraries for the project. Install with `pip install -r requirements.txt`.

Feel free to explore and run these scripts to analyze and visualize stock market data. For more details on each script and its usage, refer to the specific sections above.

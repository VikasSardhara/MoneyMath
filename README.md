# MoneyMath - Quantitative Finance Project

The MoneyMath project is a Python application for quantitative analysis, processing, and visualizing stock market data.

## Project Structure

The project consists of the following files:

1. **process_data.py**: Contains functions for processing stock data and saving it to the `output.txt` file. It is responsible for the initial processing of stock data.

2. **precise_stock_price.py**: Fetches precise stock prices for a given stock, month, and year. It is a standalone script that can be used to get precise stock prices for specific periods.

3. **live_price.py**: Fetches and displays live stock prices for specified stock symbols. It continuously updates the prices and clears the console for a clean display.

4. **arima_forecast.py**: Performs an ARIMA analysis on historical stock prices, forecasting future stock prices, and visualizing the results.

5. **stock_graph_of_each_month.py**: Generates and saves graphs for each month based on processed stock data. It uses the processed data obtained from `process_data.py` to create monthly stock price graphs.

6. **plot_graph.py**: Contains a function for plotting a graph based on the processed data. It takes the processed stock data and creates a visual representation in the form of a graph.

7. **requirements.txt**: Specifies the required libraries and their versions for the project.

8. **main.py**: Serves as the main entry point, calling functions from other files to execute the entire process. It provides a user-friendly interface for running the entire data processing and graph plotting workflow, including generating monthly graphs.

9. **lowprice_for_eachday.py**: Fetches and prints the lowest stock price for each day of a specified year. It fetches stock prices for each day using `precise_stock_price.py` and displays the lowest prices.

## Usage

To run the project, follow these steps:

1. Install the required libraries:

   ```bash
   pip install -r requirements.txt

# MoneyMath - Quantitative Finance Project

The MoneyMath project is a Python application for quantitative analysis, processing, and visualizing stock market data.

## Project Structure

The project consists of the following files:

1. **arima_forecast.py**: Performs an ARIMA (AutoRegressive Integrated Moving Average) analysis on historical stock prices, forecasting future stock prices, and visualizing the results.

2. **live_price.py**: Fetches and displays live stock prices for specified stock symbols. It continuously updates the prices and clears the console for a clean display.

3. **lowprice_for_eachday.py**: Fetches and prints the lowest stock price for each day of a specified year. It fetches stock prices for each day using `monthly_graph.py` and displays the lowest prices.

4. **monthly_graph.py**: Fetches stock prices for a given stock, month, and year. It generates and displays graphs for each day of the specified month.

5. **monthly_price_comparison.py**: Fetches and plot the graph the lowest stock price and highest stock price for each month of a specified year. 

6. **stock_graph_of_each_month.py**: Generates and saves graphs for each month based on processed stock data. It uses the processed data obtained from `monthly_graph.py` to create monthly stock price graphs.



## Usage

To run specific parts of the project, follow these steps:

### 1. Installing Dependencies

Install the required libraries:

```bash
pip install -r requirements.txt

```
## Run File

To run specific file of the project

```bash
python <file_name.py>

```

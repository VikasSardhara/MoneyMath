# arima_forecast.py
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import os
import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 4:
    print("Usage: python arima_forecast.py <stock> <month> <year>")
    sys.exit(1)

# Extract command-line arguments
stock = sys.argv[1]
month = int(sys.argv[2])
year = int(sys.argv[3])

# Run the precise_stock_price.py script with the provided arguments
os.system(f'python precise_stock_price.py {stock} {month} {year}')

# Read historical stock prices
historical_data = pd.read_csv('historical_stock_prices.csv')
historical_data['Date'] = pd.to_datetime(historical_data['Date'])
historical_data.set_index('Date', inplace=True)

# Fit ARIMA model with optimized parameters
# Hyperparameter tuning and grid search can be done to find the best values for (p, d, q)
# For simplicity, let's assume that the best parameters are (5, 1, 2)
model = ARIMA(historical_data['Low Price'], order=(5, 1, 2))
result = model.fit()

# Forecast future prices with a larger number of steps for more precise prediction
forecast_steps = 60  # Adjust the number of steps as needed
forecast = result.get_forecast(steps=forecast_steps)
forecast_index = pd.date_range(historical_data.index[-1], periods=forecast_steps + 1, freq='B')[1:]

# Set the style for a visually appealing graph (using 'ggplot' style)
plt.style.use('ggplot')

# Create a figure with a larger size and rounded corners
fig, ax = plt.subplots(figsize=(14, 8))
fig.patch.set_edgecolor('black')
fig.patch.set_linewidth(2.0)
ax.set_facecolor('#F3F3F3')

# Plot historical stock prices with a blue line
plt.plot(historical_data.index, historical_data['Low Price'], label='Historical Prices', color='#007ACC', linewidth=2)

# Plot forecasted prices with a red dashed line
plt.plot(forecast_index, forecast.predicted_mean, label='Forecasted Prices', linestyle='dashed', color='#FF4500', linewidth=2)

# Fill the area between the historical and forecasted prices for visual clarity
plt.fill_between(forecast_index, forecast.conf_int()['lower Low Price'], forecast.conf_int()['upper Low Price'], color='#FFDAB9', alpha=0.3, label='Confidence Interval')

# Set labels and title with larger fonts
plt.title('Improved ARIMA Forecast of Stock Prices', fontsize=18, fontweight='bold', color='#333333')
plt.xlabel('Date', fontsize=14, color='#555555')
plt.ylabel('Stock Price', fontsize=14, color='#555555')

# Display legend with enhanced formatting
plt.legend(loc='upper left', fontsize=12, edgecolor='#F3F3F3')

# Display the plot with a shadowed background
ax.set_facecolor('#F3F3F3')
plt.show()

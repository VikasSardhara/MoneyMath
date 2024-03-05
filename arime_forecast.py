# arima_forecast_combined.py
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from datetime import datetime, timedelta

import yfinance as yf

# Read command-line arguments
stock = input("Enter Stock Symbol: ").upper()
month = int(input("Enter number of month: "))
year = int(input("Enter year: "))

price_data = {}

for date in range(1, 31):
    last_date = (datetime(year, (month % 12) + 1, 1) - timedelta(days=1)).day
    main_date = min(date, last_date)
    startd = f"{year}-{month:02d}-01"
    endd = f"{year}-{month:02d}-{last_date:02d}"
    target = datetime(year, month, main_date)
    data = yf.download(stock, startd, endd)
    try:
        price = data.loc[target.strftime("%Y-%m-%d")]["Low"]
        price_data[target] = round(price, 2)
    except KeyError:
        print(f"No data available for {target.strftime('%Y-%m-%d')}")
    except Exception as e:
        print(f"Exception Error: {e}")

# Read historical stock prices from the original data
historical_data = pd.DataFrame(price_data.items(), columns=['Date', 'Low Price'])
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

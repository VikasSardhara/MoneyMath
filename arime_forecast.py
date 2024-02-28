# arima_forecast.py
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Read historical stock prices
historical_data = pd.read_csv('historical_stock_prices.csv')
historical_data['Date'] = pd.to_datetime(historical_data['Date'])
historical_data.set_index('Date', inplace=True)

# Fit ARIMA model
model = ARIMA(historical_data['Low Price'], order=(5, 1, 0))  # Adjust order as needed
result = model.fit()

# Forecast future prices
forecast_steps = 30  # Adjust the number of steps as needed
forecast = result.get_forecast(steps=forecast_steps)
forecast_index = pd.date_range(historical_data.index[-1], periods=forecast_steps + 1, freq='B')[1:]

# Plotting historical and forecasted prices
plt.figure(figsize=(10, 6))
plt.plot(historical_data.index, historical_data['Low Price'], label='Historical Prices', color='blue')
plt.plot(forecast_index, forecast.predicted_mean, label='Forecasted Prices', color='red')
plt.title('ARIMA Forecast of Stock Prices')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend()
plt.show()

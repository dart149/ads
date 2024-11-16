from statsmodels.tsa.holtwinters import ExponentialSmoothing
data = [3, 10, 12, 13, 12, 10, 12]
model = ExponentialSmoothing(data, trend='add').fit()
forecast = model.forecast(3)
print("Forecast:", forecast)

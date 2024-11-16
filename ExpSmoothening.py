from statsmodels.tsa.holtwinters import SimpleExpSmoothing
data = [3, 10, 12, 13, 12, 10, 12]
model = SimpleExpSmoothing(data).fit()
forecast = model.forecast(3)
print("Forecast:", forecast)

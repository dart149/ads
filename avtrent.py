import pandas as pd
import matplotlib.pyplot as plt
data = pd.DataFrame({
    'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']),
    'Value': [10, 12, 15, 13, 16]
})
data.set_index('Date', inplace=True)
data['Rolling Mean'] = data['Value'].rolling(window=3).mean()
plt.plot(data['Value'], label='Original Data')
plt.plot(data['Rolling Mean'], label='Rolling Mean (Trend)')
plt.title('Time Series Data with Trend')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

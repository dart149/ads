import pandas as pd
import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
X, y = make_regression(n_samples=100, n_features=3, noise=10, random_state=42)
df = pd.DataFrame(X, columns=['Forehead Wrinkle Count', 'Skin Elasticity', 'Hair Grayness'])
df['Age'] = y
print("Synthetic Data:")
print(df.head())
X = df[['Forehead Wrinkle Count', 'Skin Elasticity', 'Hair Grayness']]
y = df['Age']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"\nMean Squared Error: {mse}")
print(f"R² Score: {r2}")

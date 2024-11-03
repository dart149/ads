import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Sample synthetic dataset
data = {
    "Income": [45000, 54000, 58000, 60000, 65000, 72000, 82000, 85000, 95000, 110000],
    "Experience": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "Education_Level": [12, 13, 12, 16, 14, 15, 16, 18, 17, 20],
    "Age": [25, 28, 30, 32, 34, 36, 38, 40, 42, 45]
}
df = pd.DataFrame(data)

# Define features and target variable
X = df[["Income", "Experience", "Education_Level"]]
y = df["Age"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
print(y_pred)
# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Evaluation:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"R-squared Score: {r2:.2f}")

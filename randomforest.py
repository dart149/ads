import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# Example: Loan Prediction
# Create or load a dataset
# Simulated data for demonstration
data = {
    'ApplicantIncome': [2500, 3000, 4000, 5000, 6000, 2000, 1000, 4500, 5500, 7000],
    'CoapplicantIncome': [0, 1500, 0, 0, 2000, 0, 500, 1000, 0, 1500],
    'LoanAmount': [100, 200, 150, 250, 300, 120, 80, 180, 220, 350],
    'CreditHistory': [1, 0, 1, 1, 1, 0, 0, 1, 1, 1],
    'LoanStatus': [1, 0, 1, 1, 1, 0, 0, 1, 1, 1]  # 1: Approved, 0: Not Approved
}

# Step 1: Read data
df = pd.DataFrame(data)
print("Dataset:")
print(df)

# Step 2: Train-test split
X = df[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'CreditHistory']]  # Features
y = df['LoanStatus']  # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Model building
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 4: Model evaluation
y_pred = model.predict(X_test)

# Print classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Additional performance metrics
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nAccuracy Score:")
print(accuracy_score(y_test, y_pred))

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

# Create KNN classifier with k=3
knn = KNeighborsClassifier(n_neighbors=9)
knn.fit(X_train, y_train)  # Train the model

# Predict on the test set
y_pred = knn.predict(X_test)

# Calculate and display accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of KNN Classifier with k=3: {accuracy*100 :.2f}")

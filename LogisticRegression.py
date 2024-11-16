from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
texts = ["Buy now", "Limited offer", "Meeting at 5 PM", "Win a prize", "Get it now", "Special discount", "Conference call", "Claim your reward"]
labels = [1, 1, 0, 1, 1, 1, 0, 1]
texts_train, texts_test, labels_train, labels_test = train_test_split(texts, labels, test_size=0.2, random_state=42)
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(texts_train)
X_test = vectorizer.transform(texts_test) 
model = LogisticRegression()
model.fit(X_train, labels_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(labels_test, predictions)
print("Accuracy:", accuracy)
print("Predictions:", predictions)

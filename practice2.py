from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import numpy as np
import matplotlib.pyplot as plt

data = np.array([
    [1, 2, 0],
    [2, 3, 0],
    [3, 3, 0],
    [6, 8, 1],
    [7, 8, 1],
    [8, 9, 1],
    [3, 4, 0],
    [5, 6, 1]
])
X = data[:, :2]
y = data[:, 2]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

k = 3
knn_model = KNeighborsClassifier(n_neighbors=k)
knn_model.fit(X_train, y_train)
y_pred = knn_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Training data (X_train, y_train):")
print(X_train, y_train)
print("testing data (X_test, y_test):")
print(X_test, y_test)
print("Predicted labels:", y_pred)
print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap="coolwarm", label="Train data", alpha=0.7)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap="coolwarm",edgecolor="k", marker='s', label="Test Predictions")
plt.title(f"KNN Classification (k={k})")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid(True)
plt.show()
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import sys

# -----------------------------
# 1. Sample dataset creation
# -----------------------------
# In real use, load from CSV: pd.read_csv("disease_dataset.csv")
data = {
    'fever': [1, 0, 1, 0, 1, 0],
    'cough': [1, 1, 0, 0, 1, 0],
    'fatigue': [1, 0, 1, 0, 0, 1],
    'headache': [0, 1, 1, 0, 0, 1],
    'disease': ['Flu', 'Cold', 'Flu', 'Healthy', 'Flu', 'Healthy']
}

df = pd.DataFrame(data)

# -----------------------------
# 2. Features & Labels
# -----------------------------
X = df.drop('disease', axis=1)
y = df['disease']

# -----------------------------
# 3. Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# -----------------------------
# 4. Model Training
# -----------------------------
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# -----------------------------
# 5. Model Evaluation
# -----------------------------
y_pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# -----------------------------
# 6. Prediction Function
# -----------------------------
def predict_disease(fever, cough, fatigue, headache):
    try:
        # Ensure inputs are binary (0 or 1)
        for val in [fever, cough, fatigue, headache]:
            if val not in [0, 1]:
                raise ValueError("All symptom values must be 0 or 1.")
        
        prediction = model.predict([[fever, cough, fatigue, headache]])
        return prediction[0]
    except Exception as e:
        return f"Error: {e}"

# -----------------------------
# 7. Example Prediction
# -----------------------------
print("\nExample Prediction:")
print("Symptoms: fever=1, cough=1, fatigue=0, headache=0")
print("Predicted Disease:", predict_disease(1, 1, 0, 0))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

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
# 6. User Input Function
# -----------------------------
def get_symptom_input(symptom_name):
    """Ask user for symptom presence (yes/no) and return 1 or 0."""
    while True:
        user_input = input(f"Do you have {symptom_name}? (yes/no): ").strip().lower()
        if user_input in ['yes', 'y']:
            return 1
        elif user_input in ['no', 'n']:
            return 0
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

# -----------------------------
# 7. Interactive Prediction
# -----------------------------
print("\n--- Disease Prediction System ---")
fever = get_symptom_input("fever")
cough = get_symptom_input("cough")
fatigue = get_symptom_input("fatigue")
headache = get_symptom_input("headache")

prediction = model.predict([[fever, cough, fatigue, headache]])[0]
print(f"\nBased on your symptoms, the predicted disease is: {prediction}")

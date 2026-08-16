import pandas as pd
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import pickle

# 1. CREATE TRAINING DATASET
# Add more data for better accuracy
data = [
    # Flu
    (["fever", "cough", "sore throat"], "Flu"),
    (["fever", "cough", "fatigue"], "Flu"),
    (["fever", "body aches", "chills"], "Flu"),
    (["cough", "sore throat", "runny nose"], "Flu"),
    
    # Migraine
    (["headache", "nausea", "dizziness"], "Migraine"),
    (["headache", "sensitivity to light", "nausea"], "Migraine"),
    (["severe headache", "vomiting", "dizziness"], "Migraine"),
    
    # Heart Attack
    (["chest pain", "shortness of breath", "sweating"], "Heart Attack"),
    (["chest pain", "nausea", "arm pain"], "Heart Attack"),
    (["shortness of breath", "chest discomfort", "fatigue"], "Heart Attack"),
    
    # Food Poisoning
    (["abdominal pain", "diarrhea", "vomiting"], "Food Poisoning"),
    (["nausea", "vomiting", "stomach cramps"], "Food Poisoning"),
    (["diarrhea", "fever", "abdominal pain"], "Food Poisoning"),
    
    # Diabetes
    (["fatigue", "weight loss", "frequent urination"], "Diabetes"),
    (["increased thirst", "frequent urination", "blurred vision"], "Diabetes"),
    (["fatigue", "slow healing wounds", "increased hunger"], "Diabetes"),
    
    # Allergy
    (["itching", "rash", "swelling"], "Allergy"),
    (["sneezing", "runny nose", "watery eyes"], "Allergy"),
    (["skin rash", "hives", "itching"], "Allergy"),
    
    # Arthritis
    (["joint pain", "stiffness", "swelling"], "Arthritis"),
    (["joint pain", "reduced range of motion", "fatigue"], "Arthritis"),
    (["morning stiffness", "joint swelling", "pain"], "Arthritis"),
    
    # Spinal Disc Problem
    (["back pain", "numbness", "tingling"], "Spinal Disc Problem"),
    (["lower back pain", "leg pain", "weakness"], "Spinal Disc Problem"),
    (["back pain", "numbness in legs", "difficulty walking"], "Spinal Disc Problem"),
    
    # Common Cold
    (["runny nose", "sneezing", "sore throat"], "Common Cold"),
    (["cough", "runny nose", "mild fever"], "Common Cold"),
    (["congestion", "sneezing", "fatigue"], "Common Cold"),
    
    # Pneumonia
    (["cough", "fever", "difficulty breathing"], "Pneumonia"),
    (["chest pain", "cough with phlegm", "fever"], "Pneumonia"),
    (["shortness of breath", "fever", "fatigue"], "Pneumonia"),
]

# 2. CONVERT TO DATAFRAME
df = pd.DataFrame(data, columns=["Symptoms", "Disease"])
print(f"Total training samples: {len(df)}")
print(f"\nDiseases in dataset: {df['Disease'].unique()}")

# 3. ENCODE SYMPTOMS (Multi-hot encoding)
mlb = MultiLabelBinarizer()
X = mlb.fit_transform(df["Symptoms"])
print(f"\nTotal unique symptoms: {len(mlb.classes_)}")
print(f"Symptom features: {mlb.classes_}")

# 4. ENCODE DISEASE LABELS
le = LabelEncoder()
y = le.fit_transform(df["Disease"])

# 5. TRAIN/TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

print(f"\nTraining samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# 6. TRAIN MODEL
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# 7. EVALUATE MODEL
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\n{'='*50}")
print(f"MODEL PERFORMANCE")
print(f"{'='*50}")
print(f"Accuracy: {accuracy*100:.2f}%\n")
print("Classification Report:")
print(classification_report(y_test, y_pred, labels=np.unique(y_test), target_names=le.inverse_transform(np.unique(y_test))))

# 8. SAVE THE MODEL
model_data = {
    'model': model,
    'mlb': mlb,
    'le': le,
    'symptoms_list': list(mlb.classes_),
    'diseases_list': list(le.classes_)
}

with open('disease_model.pkl', 'wb') as f:
    pickle.dump(model_data, f)

print(f"\n{'='*50}")
print("✅ Model saved successfully as 'disease_model.pkl'")
print(f"{'='*50}")

# 9. TEST PREDICTION FUNCTION
def predict_disease(symptom_list, model_data):
    """Predict disease from symptoms"""
    input_vec = model_data['mlb'].transform([symptom_list])
    prediction = model_data['model'].predict(input_vec)
    probabilities = model_data['model'].predict_proba(input_vec)[0]
    
    disease = model_data['le'].inverse_transform(prediction)[0]
    confidence = max(probabilities) * 100
    
    return disease, confidence

# Test the prediction
print("\n" + "="*50)
print("TESTING PREDICTIONS")
print("="*50)

test_cases = [
    ["fever", "cough", "sore throat"],
    ["headache", "nausea"],
    ["chest pain", "sweating"],
    ["joint pain", "stiffness"]
]

for symptoms in test_cases:
    disease, confidence = predict_disease(symptoms, model_data)
    print(f"\nSymptoms: {symptoms}")
    print(f"Predicted Disease: {disease}")
    print(f"Confidence: {confidence:.2f}%")
import pickle
import numpy as np

# 1. LOAD THE SAVED MODEL
print("Loading trained model...")
with open('disease_model.pkl', 'rb') as f:
    model_data = pickle.load(f)

print("✅ Model loaded successfully!\n")

# Extract components
model = model_data['model']
mlb = model_data['mlb']
le = model_data['le']
available_symptoms = model_data['symptoms_list']
available_diseases = model_data['diseases_list']

# 2. PREDICTION FUNCTION
def predict_disease(symptom_list):
    """
    Predict disease from a list of symptoms
    
    Args:
        symptom_list: List of symptoms (e.g., ["fever", "cough"])
    
    Returns:
        disease: Predicted disease name
        confidence: Prediction confidence (0-100%)
        all_probabilities: Dictionary of all diseases and their probabilities
    """
    # Transform symptoms to feature vector
    input_vec = mlb.transform([symptom_list])
    
    # Make prediction
    prediction = model.predict(input_vec)
    probabilities = model.predict_proba(input_vec)[0]
    
    # Get predicted disease
    disease = le.inverse_transform(prediction)[0]
    confidence = max(probabilities) * 100
    
    # Get all disease probabilities
    all_probs = {
        disease_name: prob * 100 
        for disease_name, prob in zip(le.classes_, probabilities)
    }
    
    # Sort by probability
    all_probs = dict(sorted(all_probs.items(), key=lambda x: x[1], reverse=True))
    
    return disease, confidence, all_probs


# 3. INTERACTIVE PREDICTION
def interactive_prediction():
    """Interactive symptom input and prediction"""
    print("="*60)
    print("DISEASE PREDICTION SYSTEM")
    print("="*60)
    print("\nAvailable symptoms:")
    for i, symptom in enumerate(available_symptoms, 1):
        print(f"{i:2d}. {symptom}")
    
    print("\n" + "="*60)
    print("Enter symptoms (comma-separated) or type 'quit' to exit")
    print("Example: fever, cough, sore throat")
    print("="*60)
    
    while True:
        user_input = input("\nEnter symptoms: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if not user_input:
            print("⚠️  Please enter at least one symptom")
            continue
        
        # Parse symptoms
        symptoms = [s.strip().lower() for s in user_input.split(',')]
        
        # Validate symptoms
        invalid_symptoms = [s for s in symptoms if s not in available_symptoms]
        if invalid_symptoms:
            print(f"⚠️  Invalid symptoms: {invalid_symptoms}")
            print("Please use symptoms from the available list above.")
            continue
        
        # Make prediction
        disease, confidence, all_probs = predict_disease(symptoms)
        
        # Display results
        print("\n" + "-"*60)
        print("PREDICTION RESULTS")
        print("-"*60)
        print(f"Input Symptoms: {', '.join(symptoms)}")
        print(f"\n🏥 Predicted Disease: {disease}")
        print(f"📊 Confidence: {confidence:.2f}%")
        
        print("\n📋 All Disease Probabilities:")
        for disease_name, prob in all_probs.items():
            bar = "█" * int(prob / 5)  # Scale bar to 20 chars max
            print(f"  {disease_name:25s} {prob:6.2f}% {bar}")
        
        print("-"*60)


# 4. BATCH PREDICTION (for testing multiple cases)
def batch_predict(test_cases):
    """Predict multiple symptom combinations"""
    print("\n" + "="*60)
    print("BATCH PREDICTIONS")
    print("="*60)
    
    for i, symptoms in enumerate(test_cases, 1):
        disease, confidence, _ = predict_disease(symptoms)
        print(f"\n{i}. Symptoms: {symptoms}")
        print(f"   Disease: {disease} (Confidence: {confidence:.2f}%)")


# 5. MAIN EXECUTION
if __name__ == "__main__":
    # Show model info
    print("Available Diseases:", ", ".join(available_diseases))
    print(f"Total Symptoms: {len(available_symptoms)}\n")
    
    # Example batch predictions
    test_cases = [
        ["fever", "cough", "sore throat"],
        ["headache", "nausea", "sensitivity to light"],
        ["chest pain", "shortness of breath"],
        ["joint pain", "stiffness", "swelling"],
        ["runny nose", "sneezing"]
    ]
    
    batch_predict(test_cases)
    
    # Start interactive mode
    print("\n")
    interactive_prediction()
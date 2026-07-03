import os
import numpy as np
import joblib

MODEL_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model')

def predict_crop(n, p, k, temp, humidity, ph, rainfall):
    """Loads saved model, scaler, label_encoder and returns predicted crop and confidence score."""
    model_path = os.path.join(MODEL_DIR, 'model.pkl')
    scaler_path = os.path.join(MODEL_DIR, 'scaler.pkl')
    label_encoder_path = os.path.join(MODEL_DIR, 'label_encoder.pkl')
    
    if not (os.path.exists(model_path) and os.path.exists(scaler_path) and os.path.exists(label_encoder_path)):
        raise FileNotFoundError("Model files not found. Please train models first using utils/train.py")
        
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    label_encoder = joblib.load(label_encoder_path)
    
    # Preprocess inputs
    features = np.array([[n, p, k, temp, humidity, ph, rainfall]])
    features_scaled = scaler.transform(features)
    
    # Predict label
    prediction_idx = model.predict(features_scaled)[0]
    predicted_crop = label_encoder.inverse_transform([prediction_idx])[0]
    
    # Calculate confidence score if available
    confidence = None
    if hasattr(model, 'predict_proba'):
        probabilities = model.predict_proba(features_scaled)[0]
        confidence = float(np.max(probabilities))
        
    return predicted_crop, confidence

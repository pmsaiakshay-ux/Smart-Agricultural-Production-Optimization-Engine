import os
import urllib.request
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib

DATASET_URL = "https://raw.githubusercontent.com/Gladiator07/Harvestify/master/Data-processed/crop_recommendation.csv"
DATASET_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dataset', 'Crop_recommendation.csv')
MODEL_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model')

def download_dataset():
    """Downloads the Crop Recommendation Dataset if it does not exist locally."""
    if not os.path.exists(DATASET_PATH):
        print(f"Dataset not found locally. Downloading from {DATASET_URL}...")
        os.makedirs(os.path.dirname(DATASET_PATH), exist_ok=True)
        try:
            urllib.request.urlretrieve(DATASET_URL, DATASET_PATH)
            print(f"Dataset downloaded successfully and saved to {DATASET_PATH}.")
        except Exception as e:
            print(f"Error downloading dataset: {e}")
            raise e
    else:
        print("Dataset already exists locally.")

def load_and_clean_data():
    """Loads the dataset, removes duplicates, and handles missing values."""
    download_dataset()
    df = pd.read_csv(DATASET_PATH)
    
    # Remove duplicates
    initial_rows = len(df)
    df = df.drop_duplicates()
    duplicated_rows = initial_rows - len(df)
    if duplicated_rows > 0:
        print(f"Removed {duplicated_rows} duplicate rows.")
    
    # Handle missing values
    null_counts = df.isnull().sum().sum()
    if null_counts > 0:
        print(f"Found {null_counts} missing values. Filling with median/mode...")
        for col in df.columns:
            if df[col].dtype in [np.float64, np.int64]:
                df[col] = df[col].fillna(df[col].median())
            else:
                df[col] = df[col].fillna(df[col].mode()[0])
                
    return df

def prepare_data(test_size=0.2, random_state=42):
    """Preprocesses data: splits features/labels, scales, encodes labels, and train/test split."""
    df = load_and_clean_data()
    
    X = df.drop(columns=['label'])
    y = df['label']
    
    # Encode labels
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    
    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=test_size, random_state=random_state)
    
    # Feature Scaling
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Ensure model folder exists
    os.makedirs(MODEL_DIR, exist_ok=True)
    
    # Save encoders & scalers
    joblib.dump(scaler, os.path.join(MODEL_DIR, 'scaler.pkl'))
    joblib.dump(label_encoder, os.path.join(MODEL_DIR, 'label_encoder.pkl'))
    print("Saved scaler.pkl and label_encoder.pkl successfully.")
    
    return X_train_scaled, X_test_scaled, y_train, y_test, X.columns.tolist(), label_encoder

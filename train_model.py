"""
Traffic Accident Risk Detection - Model Training Script
This script trains a machine learning model to predict accident risk
"""

import os
import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
from pathlib import Path

def load_config():
    """Load configuration from config.json"""
    config_path = Path(__file__).parent / "config.json"
    with open(config_path, 'r') as f:
        return json.load(f)

def load_data(data_path):
    """Load training data from CSV"""
    print(f"Loading data from {data_path}...")
    df = pd.read_csv(data_path)
    print(f"Data shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    return df

def preprocess_data(df):
    """Preprocess data for model training"""
    print("\nPreprocessing data...")
    
    # Create a copy to avoid modifying original
    data = df.copy()
    
    # Encode categorical variables
    le_weather = LabelEncoder()
    data['weather_encoded'] = le_weather.fit_transform(data['weather'])
    
    # Features and target
    feature_columns = ['hour', 'weather_encoded', 'traffic_volume', 'avg_speed', 'speed_variance', 'visibility']
    X = data[feature_columns]
    
    # Target: convert accident_risk to binary classification (0 or 1)
    y = (data['accident_risk'] >= 0.5).astype(int)
    
    print(f"Features shape: {X.shape}")
    print(f"Target distribution: {y.value_counts().to_dict()}")
    
    return X, y, le_weather

def train_model(X, y):
    """Train the Random Forest model"""
    print("\nTraining model...")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train model
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )
    
    model.fit(X_train, y_train)
    
    # Evaluate
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    
    print(f"Training accuracy: {train_score:.4f}")
    print(f"Testing accuracy: {test_score:.4f}")
    
    # Feature importance
    print("\nFeature importance:")
    feature_names = ['hour', 'weather', 'traffic_volume', 'avg_speed', 'speed_variance', 'visibility']
    for name, importance in zip(feature_names, model.feature_importances_):
        print(f"  {name}: {importance:.4f}")
    
    return model

def save_model(model, model_path):
    """Save trained model to disk"""
    print(f"\nSaving model to {model_path}...")
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    print("Model saved successfully!")

def main():
    """Main training pipeline"""
    config = load_config()
    
    # Paths
    data_path = config['data']['training_path']
    model_path = config['model']['path']
    
    # Load and preprocess
    df = load_data(data_path)
    X, y, le_weather = preprocess_data(df)
    
    # Train
    model = train_model(X, y)
    
    # Save
    save_model(model, model_path)
    
    print("\n✅ Training complete!")
    print(f"Model saved to: {model_path}")

if __name__ == '__main__':
    main()

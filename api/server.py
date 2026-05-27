"""
Traffic Accident Risk Detection API Server
Main backend server for handling prediction requests
"""

import json
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from pathlib import Path

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configuration
CONFIG_PATH = Path(__file__).parent.parent / "config.json"

def load_config():
    """Load configuration from config.json"""
    try:
        with open(CONFIG_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: config.json not found at {CONFIG_PATH}")
        return {}

config = load_config()

# Model placeholder (replace with actual model loading when available)
MODEL = None

def load_model():
    """Load the trained model"""
    global MODEL
    try:
        model_path = config.get('model', {}).get('path', './models/risk_model.pkl')
        # TODO: Uncomment when model file is available
        # import joblib
        # MODEL = joblib.load(model_path)
        print(f"Model loaded from {model_path}")
    except Exception as e:
        print(f"Error loading model: {e}")
        print("Using mock predictions for now")

def predict_risk(data):
    """
    Calculate accident risk probability based on input parameters
    
    Args:
        data: Dictionary with keys:
            - hour: int (0-23)
            - weather: str (Clear, Rain, Fog, Snow)
            - traffic_volume: int (vehicles/hour)
            - avg_speed: int (km/h)
            - speed_variance: int
            - visibility: float (km, 0-10)
    
    Returns:
        Dictionary with risk_probability and additional factors
    """
    try:
        # Extract features
        hour = data.get('hour', 12)
        weather = data.get('weather', 'Clear')
        traffic_volume = data.get('traffic_volume', 3000)
        avg_speed = data.get('avg_speed', 50)
        speed_variance = data.get('speed_variance', 10)
        visibility = data.get('visibility', 10)
        
        # Mock prediction logic (replace with actual model prediction)
        # This is a simplified risk calculation for demonstration
        base_risk = 0.3
        
        # Hour factor (peak hours 8-9am, 5-7pm are riskier)
        if hour in [8, 9, 17, 18, 19]:
            base_risk += 0.15
        
        # Weather factor
        weather_multiplier = {
            'Clear': 1.0,
            'Rain': 1.5,
            'Fog': 2.0,
            'Snow': 2.5
        }.get(weather, 1.0)
        
        # Visibility factor (lower is riskier)
        visibility_factor = max(0, (10 - visibility) / 10) * 0.3
        
        # Speed variance factor (higher variance = riskier)
        speed_variance_factor = min(0.25, speed_variance / 100)
        
        # Traffic volume factor
        traffic_factor = min(0.3, traffic_volume / 10000)
        
        # Calculate total risk
        risk = (
            base_risk * weather_multiplier +
            visibility_factor +
            speed_variance_factor +
            traffic_factor
        ) / 4
        
        risk = min(1.0, max(0.0, risk))
        
        # Determine risk level
        if risk >= 0.7:
            risk_level = "CRITICAL"
        elif risk >= 0.5:
            risk_level = "HIGH"
        elif risk >= 0.3:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"
        
        return {
            'risk_probability': float(risk),
            'risk_level': risk_level,
            'factors': {
                'weather_impact': float(weather_multiplier - 1.0),
                'visibility_impact': float(visibility_factor),
                'speed_variance_impact': float(speed_variance_factor),
                'traffic_impact': float(traffic_factor)
            }
        }
    
    except Exception as e:
        print(f"Error in prediction: {e}")
        raise

@app.route('/api/predict', methods=['POST'])
def predict():
    """Handle prediction requests"""
    try:
        data = request.get_json()
        
        # Validate input
        required_fields = ['hour', 'weather', 'traffic_volume', 'avg_speed', 'speed_variance', 'visibility']
        missing_fields = [f for f in required_fields if f not in data]
        
        if missing_fields:
            return jsonify({
                'error': f'Missing required fields: {", ".join(missing_fields)}'
            }), 400
        
        # Get prediction
        result = predict_risk(data)
        
        return jsonify(result), 200
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Traffic Accident Risk Detection API',
        'version': config.get('app', {}).get('version', '1.0.0')
    }), 200

@app.route('/api/config', methods=['GET'])
def get_config():
    """Get API configuration (public info only)"""
    public_config = {
        'name': config.get('app', {}).get('name'),
        'version': config.get('app', {}).get('version'),
        'risk_thresholds': config.get('risk_thresholds', {})
    }
    return jsonify(public_config), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal server error'
    }), 500

if __name__ == '__main__':
    # Load model
    load_model()
    
    # Run server
    server_config = config.get('server', {})
    port = int(os.environ.get('PORT', server_config.get('port', 3000)))
    debug = server_config.get('debug', False)
    
    print(f"Starting Traffic Accident Risk Detection API on port {port}...")
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )

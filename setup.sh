#!/bin/bash

# Traffic Accident Risk Detection - Setup Script
# This script sets up the project environment and trains the model

echo "🚗 Traffic Accident Risk Detection - Setup"
echo "=========================================="

# Create directories
echo "📁 Creating directories..."
mkdir -p data models logs

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Train the model
echo "🤖 Training ML model..."
python train_model.py

echo ""
echo "✅ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "1. Start the API server: python api/server.py"
echo "2. Open index.html in your browser"
echo "3. Try making predictions!"
echo ""

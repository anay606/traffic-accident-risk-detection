# 🚗 Traffic Accident Risk Detection

An intelligent machine learning system that predicts traffic accident risk based on real-time conditions including weather, traffic volume, speed patterns, and visibility.

## 📋 Features

- **Real-time Risk Assessment**: Predict accident probability based on current traffic conditions
- **Interactive Web Interface**: User-friendly dashboard for risk predictions
- **Multi-factor Analysis**: Considers hour of day, weather, traffic volume, speed variance, and visibility
- **Risk Categorization**: Color-coded risk levels (Low, Medium, High, Critical)
- **API-driven Architecture**: RESTful backend for scalable predictions

## 🎯 Risk Levels

| Level | Range | Indicator |
|-------|-------|-----------|
| 🟢 Low | 0-29% | Safe conditions |
| 🟡 Medium | 30-49% | Caution advised |
| 🟠 High | 50-69% | Elevated risk |
| 🔴 Critical | 70%+ | Dangerous conditions |

## 📦 Project Structure

```
traffic-accident-risk-detection/
├── index.html              # Frontend interface
├── api/
│   ├── server.py           # Python backend
│   └── requirements.txt     # Python dependencies
├── models/
│   └── risk_model.pkl      # Trained ML model
├── data/
│   ├── training_data.csv   # Historical traffic data
│   └── traffic-accident-risk-detection.zip  # Complete dataset
├── .gitignore              # Git ignore patterns
├── config.json             # Configuration settings
└── README.md               # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ 
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/anay606/traffic-accident-risk-detection.git
   cd traffic-accident-risk-detection
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the backend server**
   ```bash
   python api/server.py
   ```

4. **Open the frontend**
   ```
   Open index.html in your browser or serve via HTTP server:
   python -m http.server 8000
   ```

5. **Access the application**
   ```
   http://localhost:8000
   ```

## 📊 Input Parameters

The model accepts the following parameters:

- **Hour** (0-23): Hour of the day
- **Weather**: Clear, Rain, Fog, or Snow
- **Traffic Volume**: Vehicles per hour (0+)
- **Average Speed**: km/h (0+)
- **Speed Variance**: Variation in speeds
- **Visibility**: Distance in km (0-10)

## 🤖 API Endpoint

### POST /api/predict

**Request:**
```json
{
  "hour": 18,
  "weather": "Rain",
  "traffic_volume": 4500,
  "avg_speed": 30,
  "speed_variance": 22,
  "visibility": 3
}
```

**Response:**
```json
{
  "risk_probability": 0.65,
  "risk_level": "HIGH",
  "factors": {
    "weather_impact": 0.2,
    "traffic_impact": 0.15,
    "visibility_impact": 0.3
  }
}
```

## 📈 Model Performance

- **Accuracy**: [To be updated with your model metrics]
- **Precision**: [To be updated]
- **Recall**: [To be updated]
- **F1 Score**: [To be updated]

## 📚 Dataset

The training data is included in `traffic-accident-risk-detection.zip` containing:
- Historical traffic patterns
- Weather conditions
- Accident statistics
- Time-based metrics

## 🔧 Configuration

Edit `config.json` to customize settings for the API server and ML model.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 📧 Contact

For questions or suggestions, please open an issue on [GitHub](https://github.com/anay606/traffic-accident-risk-detection).

---

**Last Updated**: May 2026
**Status**: Active Development ✅

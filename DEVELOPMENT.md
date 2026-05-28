# Development Guide

## 🛠️ Setup Development Environment

### Prerequisites

- Python 3.8+
- pip
- Git
- Virtual environment tool

### Installation

```bash
# Clone repository
git clone https://github.com/anay606/traffic-accident-risk-detection.git
cd traffic-accident-risk-detection

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r api/requirements.txt
```

## Running the Application

### Start Backend API

```bash
python api/server.py
```

Server runs on `http://localhost:3000`

### Serve Frontend (in another terminal)

```bash
python -m http.server 8000
```

Frontend at `http://localhost:8000`

## Testing

### Run Unit Tests

```bash
pytest api/tests/ -v
```

### Run with Coverage

```bash
pytest api/tests/ --cov=api --cov-report=html
```

### Manual API Testing

```bash
# Health check
curl http://localhost:3000/api/health

# Config
curl http://localhost:3000/api/config

# Prediction
curl -X POST http://localhost:3000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "hour": 18,
    "weather": "Rain",
    "traffic_volume": 4500,
    "avg_speed": 30,
    "speed_variance": 22,
    "visibility": 3
  }'
```

## Code Quality

### Linting
```bash
flake8 api/
```

### Code Formatting
```bash
black api/
```

## Training the Model

```bash
python train_model.py
```

Requires `data/training_data.csv`

## Git Workflow

1. Create feature branch
   ```bash
   git checkout -b feature/your-feature
   ```

2. Make changes and commit
   ```bash
   git add .
   git commit -m "Add your changes"
   ```

3. Push to remote
   ```bash
   git push origin feature/your-feature
   ```

4. Create Pull Request on GitHub

## Project Structure

```
.
├── api/
│   ├── server.py              # Flask API
│   ├── requirements.txt        # Dependencies
│   └── tests/
│       ├── __init__.py
│       └── test_api.py         # Unit tests
├── models/
│   └── risk_model.pkl          # Trained model
├── data/
│   └── training_data.csv       # Training data
├── index.html                  # Frontend UI
├── config.json                 # Configuration
├── train_model.py              # Model training
├── Dockerfile                  # Container build
├── docker-compose.yml          # Full stack
├── DEPLOYMENT.md               # Deploy guide
└── DEVELOPMENT.md              # This file
```

## Common Issues

### Port Already in Use
```bash
lsof -i :3000
kill -9 <PID>
```

### Model Not Found
```bash
python train_model.py
```

### CORS Errors
Check `config.json` CORS settings

---

**Last Updated**: May 2026

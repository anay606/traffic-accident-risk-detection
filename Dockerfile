# Multi-stage build for Traffic Accident Risk Detection
FROM python:3.9-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY api/requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Production stage
FROM python:3.9-slim

# Set up a safe system user required by Hugging Face 
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PORT=7860

WORKDIR $HOME/app

# Install runtime dependencies (Must be done as root)
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*
USER user

# Copy Python dependencies from builder
COPY --from=builder --chown=user /root/.local $HOME/.local

# Copy application code with correct user permissions
COPY --chown=user api/ ./api/
COPY --chown=user config.json .
COPY --chown=user models/ ./models/
COPY --chown=user index.html .

# Health check (Updated to use port 7860)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:7860/api/health || exit 1

# Expose Hugging Face's port
EXPOSE 7860

# Run the application
CMD ["python", "api/server.py"]

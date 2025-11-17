# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies required by WeasyPrint
# Based on official WeasyPrint documentation for Debian/Ubuntu
RUN apt-get update && apt-get install -y \
    # Required for WeasyPrint with wheel support
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libharfbuzz-subset0 \
    # Additional dependencies for building from source (if needed)
    libjpeg-dev \
    libopenjp2-7-dev \
    libffi-dev \
    # Clean up to reduce image size
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY main.py .
COPY templates/ ./templates/

# Create output directory
RUN mkdir -p outputs

# Run the application
CMD ["python", "main.py"]

# Use a multi-stage build for better optimized images
FROM python:3.9-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Install dependencies
FROM base AS builder
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Prepare the final image
FROM base
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY . .

# Create a non-root user and switch to it
RUN useradd -m myuser
USER myuser

# Health check configuration
HEALTHCHECK CMD curl --fail http://localhost:8000/ || exit 1

# Command to run Gunicorn server
CMD ["gunicorn", "-b", "0.0.0.0:8000", "myapp:app"]
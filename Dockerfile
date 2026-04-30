FROM python:3.9-slim

WORKDIR /app

# Instalăm dependențele direct în imaginea finală
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiem restul codului
COPY . .

# Expunem portul
EXPOSE 8000

# Pornim aplicația
CMD ["gunicorn", "-b", "0.0.0.0:8000", "myapp:app"]
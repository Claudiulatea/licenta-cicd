FROM python:3.9-slim

WORKDIR /app

# Copiem fișierul de dependențe în container
COPY requirements.txt .

# Instalăm bibliotecile necesare
RUN pip install --no-cache-dir -r requirements.txt

# Copiem tot restul codului în container
COPY . .

# Expunem portul pe care va asculta aplicația
EXPOSE 8000

# Pornim aplicația folosind Gunicorn (încarcă instanța app din app.py)
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]

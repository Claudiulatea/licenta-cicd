# Pasul 1: Imaginea de baza
FROM python:3.9-slim

# Pasul 2: Folderul de lucru
WORKDIR /app

# Pasul 3: Instalare dependente
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pasul 4: Copiere cod sursa
COPY . .

# Pasul 5: Portul expus
EXPOSE 5000

# Pasul 6: Pornire aplicatie
CMD ["python", "app.py"]
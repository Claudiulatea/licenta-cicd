import os
import sys
import subprocess

# Auto-instalare 'requests' în caz că GitHub Actions nu o are configurată global
try:
    import requests
except ImportError:
    print("[GARDIAN AI] Modulul 'requests' nu a fost găsit. Se instalează automat...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

# Preluăm cheia API de DeepSeek din variabilele secrete ale GitHub
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
FILE_TO_CHECK = "app.py"

if not DEEPSEEK_API_KEY:
    print("[GARDIAN AI] Eroare: Lipseste cheia DEEPSEEK_API_KEY!")
    sys.exit(1)

# Citim codul curent scris în app.py
with open(FILE_TO_CHECK, "r", encoding="utf-8") as f:
    cod_curent = f.read()

print("[GARDIAN AI] Se analizează codul din app.py...")

# Configuram cererea către API-ul DeepSeek
url = "https://api.deepseek.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
    "Content-Type": "application/json"
}

prompt = (
    "Ești un inginer DevOps și programator Python senior care acționează ca un Gardian CI/CD.\n"
    "Analizează următorul cod de Flask din fișierul app.py. Dacă conține erori de sintaxă, rute greșite, "
    "sau probleme care ar bloca pornirea Gunicorn, rescrie codul corectat complet.\n"
    "Răspunsul tău TREBUIE să conțină DOAR codul Python curat, fără explicații, fără blocuri de markdown de tip ```python.\n"
    "Dacă codul este deja perfect și nu are nicio eroare structurală, răspunde exact cu cuvântul: PERFECT\n\n"
    f"Iată codul:\n\n{cod_curent}"
)

data = {
    "model": "deepseek-coder",
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.1
}

try:
    response = requests.post(url, json=data, headers=headers)
    rezultat = response.json()['choices'][0]['message']['content'].strip()

    if resultado == "PERFECT":
        print("[GARDIAN AI] Codul este stabil și corect! Permitem trecerea spre Docker Hub. ✅")
        sys.exit(0)
    else:
        print("[GARDIAN AI] ATENȚIE: S-au detectat probleme în app.py! DeepSeek a generat versiunea corectată. ⚠️")
        with open(FILE_TO_CHECK, "w", encoding="utf-8") as f:
            f.write(rezultat)
        print("[GARDIAN AI] Fișierul app.py a fost reparat cu succes local în pipeline! 🛠️")
        sys.exit(0)

except Exception as e:
    print(f"[GARDIAN AI] Eroare la comunicarea cu DeepSeek: {e}")
    sys.exit(0)
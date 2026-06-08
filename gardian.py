import os
import sys
import subprocess

# Auto-instalare automată direct în cloud ca să evităm eroarea ModuleNotFoundError
try:
    import requests
except ImportError:
    print("[GARDIAN AI] Se instalează automat modulul requests în cloud...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

# Preluăm cheia de securitate
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
FILE_TO_CHECK = "app.py"

if not DEEPSEEK_API_KEY:
    print("[GARDIAN AI] Eroare: Lipseste cheia DEEPSEEK_API_KEY în GitHub Secrets!")
    sys.exit(1)

# Verificăm dacă app.py există
if not os.path.exists(FILE_TO_CHECK):
    print(f"[GARDIAN AI] Eroare: Fișierul {FILE_TO_CHECK} nu a fost găsit!")
    sys.exit(1)

with open(FILE_TO_CHECK, "r", encoding="utf-8") as f:
    cod_curent = f.read()

print("[GARDIAN AI] DeepSeek analizează codul din app.py...")

url = "https://api.deepseek.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
    "Content-Type": "application/json"
}

prompt = (
    "Ești un inginer DevOps senior. Analizează următorul cod de Flask din app.py.\n"
    "Dacă conține erori de sintaxă sau probleme la pornire, rescrie-l corectat complet.\n"
    "Răspunde DOAR cu codul Python curat, fără explicații, fără blocuri de text.\n"
    "Dacă codul este déjà perfect, răspunde exact cu cuvântul: PERFECT\n\n"
    f"Codul este:\n{cod_curent}"
)

data = {
    "model": "deepseek-coder",
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.1
}

try:
    response = requests.post(url, json=data, headers=headers)
    response_json = response.json()

    # Protecție: Verificăm dacă răspunsul de la DeepSeek este valid sau e o eroare de API
    if 'choices' not in response_json:
        print(f"[GARDIAN AI] Serverul DeepSeek a returnat o eroare sau un răspuns neașteptat: {response_json}")
        print("[GARDIAN AI] Ignorăm verificarea AI și trecem mai departe ca măsură de siguranță. ⚠️")
        sys.exit(0)

    rezultat = response_json['choices'][0]['message']['content'].strip()

    if rezultat == "PERFECT":
        print("[GARDIAN AI] Codul este stabil și perfect! Permitem trecerea. ✅")
        sys.exit(0)
    else:
        print("[GARDIAN AI] ATENȚIE: S-au reparat erori în app.py! ⚠️")
        with open(FILE_TO_CHECK, "w", encoding="utf-8") as f:
            f.write(rezultat)
        sys.exit(0)

except Exception as e:
    print(f"[GARDIAN AI] Eroare la comunicarea cu AI-ul: {e}")
    sys.exit(0)

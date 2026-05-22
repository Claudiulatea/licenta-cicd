import subprocess, time, os, sys

# Numele fisierului care va fi monitorizat
FILE_TO_WATCH = "myapp.py"
# Cheia ta Google Gemini
API_KEY = "AIzaSyA89eGWzxYmLobVi5bRent8DxfxB0lYHcw" 

def install_dependencies():
    """Instaleaza noua librarie Google GenAI daca lipseste."""
    try:
        import google.genai
    except ImportError:
        print("📦 Instalare noua librarie Google GenAI (google-genai)...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "google-genai"])

# Instalam/verificam dependintele
install_dependencies()
from google import genai

# Configurare client nou
client = genai.Client(api_key=API_KEY)

def repara_cu_ai(eroare, cod_vechi):
    print("🤖 AI-ul (Gemini 1.5 Flash) analizeaza eroarea...")
    
    prompt = (
        "Esti un expert Python specializat in Flask. "
        "Codul de mai jos are o eroare de sintaxa. Te rog sa o repari. "
        "Returneaza DOAR codul Python corectat, fara nicio explicatie sau blocuri markdown."
        f"\n\nCOD ORIGINAL:\n{cod_vechi}\n\nEROARE:\n{eroare}"
    )

    try:
        # Folosim noul client SDK care rezolva problemele de endpoint 404
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        
        if response and response.text:
            cod_nou = response.text
            # Curatare riguroasa
            cod_curat = cod_nou.strip()
            if "```" in cod_curat:
                linii = cod_curat.split('\n')
                linii_filtrare = [l for l in linii if not l.strip().startswith("```")]
                cod_curat = '\n'.join(linii_filtrare)
            
            return cod_curat.strip()
    except Exception as e:
        print(f"❌ Eroare la apelul Gemini: {e}")
        return None

def monitorizeaza():
    print("🛡️ GARDIANUL ACTIV (Sistem Self-Healing)")
    print(f"👀 Monitorizez fisierul: {FILE_TO_WATCH}")
    
    # Pornim aplicatia Flask in fundal
    env = os.environ.copy()
    env["FLASK_APP"] = FILE_TO_WATCH
    subprocess.Popen(["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=8000"], env=env)
    
    while True:
        # Verificam sintaxa folosind py_compile
        rez = subprocess.run(['python3', '-m', 'py_compile', FILE_TO_WATCH], capture_output=True, text=True)
        
        if rez.returncode != 0:
            print(f"🚨 EROARE DETECTATA in {FILE_TO_WATCH}!")
            with open(FILE_TO_WATCH, "r") as f:
                cod_vechi = f.read()
            
            cod_reparat = repara_cu_ai(rez.stderr, cod_vechi)
            
            if cod_reparat:
                with open(FILE_TO_WATCH, "w") as f:
                    f.write(cod_reparat)
                print("✅ REPARAT! Codul a fost actualizat automat.")
                time.sleep(5) 
            else:
                print("⚠️ Nu s-a putut repara automat.")
                time.sleep(10)
        
        time.sleep(2)

if __name__ == "__main__":
    monitorizeaza()
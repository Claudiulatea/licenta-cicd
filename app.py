from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return """
    <body style="background:#1e1e2f; color:white; display:flex; justify-content:center; align-items:center; height:100vh; font-family:sans-serif;">
        <div style="background:#2a2a40; padding:50px; border-radius:15px; text-align:center; box-shadow:0 10px 30px rgba(0,0,0,0.5); border-top:6px solid #00d2ff;">
            <h1>🚀 Proiect Maistru v3.2</h1>
            <p style="color:#ccc;">Sistem CI/CD Automatizat funcțional!</p>
            <div style="background:linear-gradient(90deg, #00d2ff, #3a7bd5); padding:15px; border-radius:8px; font-weight:bold;">STATUS: LIVE ✅</div>
        </div>
    </body>
    """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
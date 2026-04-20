from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Această variabilă stochează tot design-ul nou (HTML și CSS)
    html_modern = """
    <!DOCTYPE html>
    <html lang="ro">
    <head>
        <meta charset="UTF-8">
        <title>Proiect Licență CI/CD</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #1e1e2f; /* Fundal bleumarin închis */
                color: #ffffff;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background-color: #2a2a40; /* Card de culoare gri-albăstrui */
                padding: 50px;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
                text-align: center;
                border-top: 6px solid #00d2ff;
                max-width: 500px;
            }
            h1 {
                margin-top: 0;
                color: #00d2ff;
                font-size: 28px;
            }
            p {
                color: #cccccc;
                font-size: 16px;
                line-height: 1.5;
            }
            .status-box {
                margin-top: 30px;
                padding: 15px;
                background: linear-gradient(90deg, #00d2ff 0%, #3a7bd5 100%);
                color: white;
                border-radius: 8px;
                font-weight: bold;
                font-size: 18px;
                box-shadow: 0 4px 15px rgba(0, 210, 255, 0.4);
            }
            .footer {
                margin-top: 30px;
                font-size: 12px;
                color: #666;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Sistem CI/CD Automatizat</h1>
            <p>Acest mediu de producție este actualizat în timp real, direct din repository-ul GitHub, folosind Docker și GitHub Actions.</p>
            
            <div class="status-box">
                Status: Versiunea 3.1 Live! 🚀
            </div>
            
            <div class="footer">
                Dezvoltat pentru lucrarea de diplomă | Mediu: Vagrant/Ubuntu
            </div>
        </div>
    </body>
    </html>
    """
    return html_modern

if __name__ == '__main__':
    # Rulăm aplicația pe portul 5000, accesibilă din exteriorul containerului
    app.run(host='0.0.0.0', port=5000)
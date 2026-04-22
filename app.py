from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="ro">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dashboard Licenta CI/CD</title>
        <style>
            :root {
                --primary: #00d2ff;
                --secondary: #3a7bd5;
                --bg: #0f172a;
                --card: #1e293b;
            }
            body {
                margin: 0;
                font-family: 'Segoe UI', Roboto, sans-serif;
                background: var(--bg);
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                overflow: hidden;
            }
            .container {
                text-align: center;
                background: var(--card);
                padding: 3rem;
                border-radius: 24px;
                box-shadow: 0 20px 50px rgba(0,0,0,0.5);
                border: 1px solid rgba(255,255,255,0.1);
                max-width: 500px;
                position: relative;
            }
            h1 {
                margin: 0;
                font-size: 2.5rem;
                background: linear-gradient(45deg, var(--primary), var(--secondary));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                animation: fadeIn 2s ease-in;
            }
            .rocket {
                font-size: 50px;
                display: inline-block;
                animation: launch 3s infinite ease-in-out;
            }
            .status-badge {
                display: inline-block;
                margin-top: 20px;
                padding: 8px 20px;
                background: rgba(0, 210, 255, 0.1);
                border: 1px solid var(--primary);
                color: var(--primary);
                border-radius: 50px;
                font-weight: bold;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
            .footer {
                margin-top: 30px;
                font-size: 0.9rem;
                opacity: 0.6;
            }
            @keyframes launch {
                0%, 100% { transform: translateY(0) rotate(-45deg); }
                50% { transform: translateY(-20px) rotate(-45deg); }
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: scale(0.9); }
                to { opacity: 1; transform: scale(1); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="rocket">🚀</div>
            <h1>Flux CI/CD v6.0</h1>
            <div class="status-badge">Sistem Online</div>
            <p>Aplicația a fost construită în GitHub Actions și deploy-ată prin Docker Hub.</p>
            <div class="footer">Proiect Licență &copy; 2026 - Automatizare Completă</div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
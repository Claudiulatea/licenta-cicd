from flask import Flask, render_template_string
import platform
import socket

app = Flask(__name__)

@app.route('/')
def index():
    html = """
    <!DOCTYPE html>
    <html lang="ro">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>TOP SECRET // DASHBOARD</title>
        <style>
            :root {
                --neon-green: #00ff41;
                --dark-bg: #0a0a0a;
                --panel-bg: rgba(15, 20, 15, 0.85);
            }
            body {
                margin: 0;
                padding: 0;
                background-color: var(--dark-bg);
                /* Fundal cu pattern de grid subtil */
                background-image: 
                    radial-gradient(circle at center, #50ffc099 0%, #000 100%),
                    linear-gradient(rgba(0, 255, 65, 0.03) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(0, 255, 65, 0.03) 1px, transparent 1px);
                background-size: 100% 100%, 30px 30px, 30px 30px;
                font-family: 'Courier New', Courier, monospace;
                color: var(--neon-green);
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                overflow: hidden;
            }
            .container {
                background: rgb(56 56 56 / 85%);
                border: 1px solid rgba(0, 255, 65, 0.3);
                box-shadow: 0 0 25px rgba(0, 255, 65, 0.1), inset 0 0 15px rgba(0, 255, 65, 0.05);
                border-radius: 5px;
                padding: 40px;
                max-width: 600px;
                width: 90%;
                backdrop-filter: blur(10px);
                position: relative;
            }
            /* Eticheta 'Classified' din coltul stanga-sus */
            .container::before {
                content: 'TOP SECRET // CLASSIFIED';
                position: absolute;
                top: -10px;
                left: 20px;
                background: var(--dark-bg);
                padding: 0 10px;
                font-size: 0.75em;
                letter-spacing: 2px;
                color: #555;
                border: 1px solid rgba(0, 255, 65, 0.2);
            }
            h1 {
                font-size: 1.8em;
                margin-top: 0;
                text-transform: uppercase;
                text-shadow: 0 0 5px var(--neon-green);
                border-bottom: 1px solid rgba(0, 255, 65, 0.3);
                padding-bottom: 15px;
            }
            h3 {
                color: #ffffff;
                font-weight: normal;
                font-size: 1em;
                margin-bottom: 30px;
                line-height: 1.4;
            }
            .data-row {
                display: flex;
                justify-content: space-between;
                margin-bottom: 15px;
                padding: 12px;
                background: rgba(0, 255, 65, 0.03);
                border-left: 3px solid var(--neon-green);
                transition: background 0.3s;
            }
            .data-row:hover {
                background: rgba(0, 255, 65, 0.08);
            }
            .label {
                color: #fff;
                font-weight: bold;
            }
            .value {
                font-weight: bold;
                text-align: right;
            }
            .status-badge {
                background: var(--neon-green);
                color: #000;
                padding: 2px 10px;
                border-radius: 2px;
                animation: pulse 2s infinite;
                font-weight: bold;
            }
            footer {
                margin-top: 30px;
                text-align: center;
                font-size: 0.75em;
                color: #444;
                border-top: 1px dashed rgba(0, 255, 65, 0.2);
                padding-top: 15px;
                letter-spacing: 1px;
            }
            @keyframes pulse {
                0% { opacity: 1; }
                50% { opacity: 0.5; }
                100% { opacity: 1; }
            }
            /* Media Query pentru telefoane/ecrane mici */
            @media (max-width: 480px) {
                .data-row {
                    flex-direction: column;
                }
                .value {
                    text-align: left;
                    margin-top: 8px;
                }
                h1 {
                    font-size: 1.5em;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Uplink Stabilizat 🔒</h1>
            <h3>Salut Miezu! Pipeline-ul CI/CD a fost executat cu succes. Acces autorizat.</h3>
            
            <div class="data-row">
                <span class="label">SYS_STATUS:</span>
                <span class="value"><span class="status-badge">ONLINE</span></span>
            </div>
            
            <div class="data-row">
                <span class="label">VERSIUNE_KERNEL:</span>
                <span class="value">3.0 (Stealth Mode Actions)</span>
            </div>
            
            <div class="data-row">
                <span class="label">ID_CONTAINER:</span>
                <span class="value">{{ hostname }}</span>
            </div>
            
            <div class="data-row">
                <span class="label">OS_FINGERPRINT:</span>
                <span class="value" style="font-size: 0.85em; color: #888;">{{ os_info }}</span>
            </div>
            
            <footer>
                ENCRYPTED DEPLOY // VAGRANT + DOCKER + GITHUB
            </footer>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, 
                                  hostname=socket.gethostname(), 
                                  os_info=platform.platform())

if __name__ == '__main__':
    # Rulam pe portul 8000, exact cum mapează Vagrant!
    app.run(host='0.0.0.0', port=8000)
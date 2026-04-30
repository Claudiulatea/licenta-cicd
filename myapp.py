from flask import Flask, render_template_string
import platform
import socket

app = Flask(__name__)

@app.route('/')
def index():
    html = """
    <html>
        <head><title>Dashboard Licenta</title></head>
        <body style="font-family: Arial, sans-serif; background-color: #f4f4f9; text-align: center; padding: 50px;">
            <div style="background: white; display: inline-block; padding: 30px; border-radius: 15px; shadow: 0 4px 8px rgba(0,0,0,0.1);">
                <h1 style="color: #333;">🚀 Monitorizare Proiect Licenta</h1>
                <hr>
                <p><strong>Status Aplicatie:</strong> <span style="color: green;">FUNCTIONAL</span></p>
                <p><strong>Versiune:</strong> 1.0 (Fresh Build)</p>
                <p><strong>Hostname Container:</strong> {{ hostname }}</p>
                <p><strong>Sistem Operare:</strong> {{ os_info }}</p>
                <hr>
                <footer style="font-size: 0.8em; color: #888;">Deploy realizat prin Vagrant + Docker + CI/CD</footer>
            </div>
        </body>
    </html>
    """
    return render_template_string(html, 
                                hostname=socket.gethostname(), 
                                os_info=platform.platform())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
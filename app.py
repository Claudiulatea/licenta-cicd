from flask import Flask, render_template_string
import platform
import socket

app = Flask(__name__)

@app.route('/')
def index():
    html = """
    <html>
        <head><title>Dashboard Licenta</title></head>
        <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                     background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); 
                     color: #333;
                     text-align: center; 
                     padding: 50px; 
                     margin: 0; 
                     height: 100vh;">
            
            <div style="background: rgba(255, 255, 255, 0.95); 
                        display: inline-block; 
                        padding: 40px; 
                        border-radius: 20px; 
                        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
                        margin-top: 50px;">
                
                <h1 style="color: #2c3e50; margin-bottom: 10px;">🚀 Testare Automată Reușită!</h1>
                <h3 style="color: #27ae60; margin-top: 0;">Salut Claudiuuu! Pipeline-ul CI/CD funcționează perfect.</h3>
                <hr style="border: 0; height: 1px; background: #eee; margin: 20px 0;">
                
                <p><strong>Status Aplicație:</strong> <span style="background: #27ae60; color: white; padding: 3px 10px; border-radius: 10px; font-size: 0.9em;">ONLINE</span></p>
                <p><strong>Versiune:</strong> 2.0 (Deploy Automat GitHub Actions)</p>
                <p><strong>Hostname Container:</strong> <code style="background: #f4f4f4; padding: 2px 5px;">{{ hostname }}</code></p>
                <p><strong>Sistem Operare:</strong> <small>{{ os_info }}</small></p>
                
                <hr style="border: 0; height: 1px; background: #eee; margin: 20px 0;">
                <footer style="font-size: 0.8em; color: #666;">Deploy realizat prin <b>Vagrant + Docker + GitHub Actions</b></footer>
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
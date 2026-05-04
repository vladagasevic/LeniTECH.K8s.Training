from flask import Flask, render_template_string
import os
import socket

app = Flask(__name__)

@app.route('/')
def index():
    pod_name = socket.gethostname()
    pod_ip = socket.gethostbyname(pod_name)
    
    app_version = os.getenv("APP_VERSION", "v1.0")
    bg_color = os.getenv("APP_COLOR", "#f0f2f5")  
    db_password = os.getenv("DB_PASSWORD", "NIJE PODEŠENO")

    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>LeniTECH K8s Demo</title>
        <style>
            body { background-color: {{ bg_color }}; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .card { background: white; padding: 40px; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); text-align: center; width: 400px; }
            h1 { color: #333; margin-bottom: 20px; }
            .info { text-align: left; background: #f9f9f9; padding: 15px; border-radius: 8px; margin-top: 20px; border-left: 5px solid #007bff; }
            .status { font-weight: bold; color: {% if db_password != 'NIJE PODEŠENO' %} green {% else %} red {% endif %}; }
            .version { font-size: 1.2em; color: #007bff; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="card">
            <img src="k8s-logo.png" width="50" alt="K8s Logo">
            <h1>K8s Training</h1>
            <div class="version">Verzija: {{ app_version }}</div>
            
            <div class="info">
                <p><strong>Pod Hostname:</strong> <br> {{ pod_name }}</p>
                <p><strong>Pod IP:</strong> {{ pod_ip }}</p>
                <p><strong>DB Password:</strong> <span class="status">{{ db_password }}</span></p>
            </div>
            <p style="font-size: 0.8em; color: #666; margin-top: 20px;">Osvežite stranicu (F5) da vidite Load Balancing</p>
        </div>
    </body>
    </html>
    """
    
    return render_template_string(html_template, 
                                 pod_name=pod_name, 
                                 pod_ip=pod_ip, 
                                 app_version=app_version, 
                                 bg_color=bg_color, 
                                 db_password=db_password)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)

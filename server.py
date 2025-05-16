from flask import Flask, render_template, send_from_directory
from threading import Thread
import os

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home():
    return render_template('home.html')

# Route pour la politique de confidentialité
@app.route('/politique')
def politique():
    return render_template('politique.html')

# Route pour la page news
@app.route('/news')
def news():
    return render_template('news.html')

# Route pour la page github
@app.route('/github')
def github():
    return render_template('github.html')

# Route pour la page bio
@app.route('/bio-admin')
def github():
    return render_template('bio-admin.html')
    
def run():
    app.run(host='0.0.0.0', port=5000)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()

if __name__ == '__main__':
    run()

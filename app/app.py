from flask import Flask, request, Response, render_template, stream_with_context
from flask_cors import CORS
from api import api_bp

app = Flask(__name__)
CORS(app)  # Configura o CORS para permitir solicitações de qualquer origem

app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def index():
    return render_template('app.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

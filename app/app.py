from flask import Flask, request, Response, render_template, stream_with_context
from flask_cors import CORS
from ollama import Ollama

app = Flask(__name__)
CORS(app)  # Configura o CORS para permitir solicitações de qualquer origem

@app.route('/')
def index():
    return render_template('app.html')

@app.route('/api/generate', methods=['POST'])
def generate():
    ai = Ollama("http://localhost:11434/api/generate")  # URL do serviço externo
    return Response(stream_with_context(ai.generate(request.json['prompt'])), content_type='application/json')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

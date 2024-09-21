from flask import Flask, Blueprint, request, Response, stream_with_context, jsonify
from ollama import Ollama

app = Flask(__name__)

# Criação de um blueprint para a API
api_bp = Blueprint('api', __name__)

# Instância da classe Ollama com o URL da API externa
ollama = Ollama("http://localhost:11434/api/generate")  # URL do serviço externo de IA

@api_bp.route('/')
def index():
    return "<h1>API route</h1>"

@api_bp.route('/generate', methods=['POST'])
def generate():
    # Verifica se o corpo da requisição contém um JSON e o campo 'prompt'
    if not request.json or 'prompt' not in request.json:
        return jsonify({'error': 'O campo "prompt" é obrigatório'}), 400

    prompt = request.json['prompt']

    # Utiliza stream para retornar a resposta em partes, se necessário
    return Response(stream_with_context(ollama.generate(prompt)), content_type='application/json')

# Registra o blueprint no aplicativo Flask
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)

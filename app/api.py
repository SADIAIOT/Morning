from flask import Flask, Blueprint, render_template,redirect, url_for
from ollama import Ollama

api_bp = Blueprint('api', __name__)


@api_bp.route('/')
def index():
    return "<h1>API route</h1>"

@api_bp.route('/generate', methods=['POST'])
def generate():
    ai = Ollama("http://localhost:11434/api/generate")  # URL do serviço externo
    return Response(stream_with_context(ai.generate(request.json['prompt'])), content_type='application/json')
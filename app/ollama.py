import requests
import json

class Ollama:
    def __init__(self, url):
        self.url = url

    def generate(self, prompt):
        data = {"model": "phi3", "prompt": prompt}

        # Enviando a solicitação POST
        response = requests.post(self.url, json=data, stream=True)

        # Processando a resposta linha por linha
        for line in response.iter_lines():
            if line:
                try:
                    # Decodifica e processa cada linha JSON
                    decoded_line = json.loads(line.decode("utf-8"))
                    if "response" in decoded_line:
                        yield json.dumps(decoded_line) + "\n"
                    if decoded_line.get("done", False):
                        break
                except json.JSONDecodeError:
                    print("Erro ao decodificar JSON:", line)

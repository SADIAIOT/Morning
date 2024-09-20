# Usa uma imagem base do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo requirements.txt para o container
COPY requirements.txt .

# Instala as dependências
RUN pip install -r requirements.txt

# Copia o restante do código da aplicação para o container1

COPY . .

# Abre a porta para o mundo exterior
EXPOSE 5000

# Comando para iniciar o app Flask
CMD [ "python", "app/app.py" ]

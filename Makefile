NAME = morning

$(NAME):
	python3 app/app.py

install:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

venv:
	. venv/bin/activate
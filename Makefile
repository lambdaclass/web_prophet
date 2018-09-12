.PHONY: install run

install:
	pip install -r requirements.txt

run:
	bash -c "export FLASK_APP=app.py && flask run"

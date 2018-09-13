.PHONY: deps start

deps:
	pipenv install

start:
	bash -c "export FLASK_APP=app.py && pipenv run flask run"

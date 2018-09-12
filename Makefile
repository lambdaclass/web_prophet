.PHONY: install run

install:
	pipenv install

run:
	bash -c "export FLASK_APP=app.py && pipenv run flask run"

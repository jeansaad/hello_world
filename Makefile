PYTHON=python3

all: requirements.txt

requirements.txt: clean venv requirements-to-freeze.txt
	venv/bin/pip install -r requirements-to-freeze.txt
	venv/bin/pip freeze -r requirements-to-freeze.txt > requirements.txt

venv:
	${PYTHON} -m venv venv

test: lint
	${PYTHON} setup.py test

lint:
	flake8

dist:
	${PYTHON} setup.py sdist

clean:
	-rm -r venv

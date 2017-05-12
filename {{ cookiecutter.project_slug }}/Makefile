.PHONY: docs

all: install migrate run

docs:
	cd docs && make clean && make html

flake8:
	flake8 --exclude=migrations,tests src

install:
	pip install -e .[docs,test]

isort:
	isort --recursive --check-only --diff src tests

lint: flake8 isort

migrate:
	python manage.py migrate

run:
	python manage.py runserver 0.0.0.0:8000

test:
	py.test tests

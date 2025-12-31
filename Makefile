.PHONY: test lint format coverage all

test:
	python -m pytest

lint:
	flake8 .

format:
	black .

coverage:
	python -m pytest --cov=app --cov-report=term-missing

all: format lint coverage

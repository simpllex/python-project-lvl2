install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	python -m pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	@poetry build
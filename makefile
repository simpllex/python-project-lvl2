install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	python -m pytest
test-coverage:
	python -m pytest --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	@poetry build
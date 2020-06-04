install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	python -m pytest
selfcheck:
	poetry check

check: selfcheck test lint

build: check
	@poetry build
install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest --cov=gendiff tests/ --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	@poetry build
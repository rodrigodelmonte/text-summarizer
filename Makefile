PHONY: build run test-coverage lint clean

setup-pre-commit:
	pip install pre-commit
	pre-commit install

build:
	docker-compose build

run:
	docker-compose up -d

create-db:
	docker-compose exec web python app/db.py

test:
	docker-compose exec web python -m pytest

test-coverage:
	docker-compose exec web python -m pytest --cov="."

lint:
	docker-compose exec web isort .
	docker-compose exec web black .
	docker-compose exec web flake8 .

security-check:
	docker-compose exec web bandit -r app/

clean:
	docker-compose stop
	docker-compose rm -f

db-access:
	docker-compose exec web-db psql -U postgres

.PHONY: up down check format

up:
	docker compose up -d --build

down:
	docker compose down -v

check:
	poetry run ruff check src --fix

format:
	poetry run ruff format src

.DEFAULT_GOAL := up

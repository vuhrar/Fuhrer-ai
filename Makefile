install:
	pip install -e .

dev:
	uvicorn backend.main:app --reload

test:
	pytest

lint:
	ruff check .

format:
	black .

typecheck:
	mypy backend

all:
	make format
	make lint
	make typecheck
	make test

fmt:
    uv run ruff format .

lint:
    uv run ruff check .

test:
    uv run pytest

check: fmt lint test

build:
    rm -rf dist/
    uv run python -m build

release: check build
    uv run twine upload dist/*

deploy:
    railway up -c
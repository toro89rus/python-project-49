install:
	uv sync

lint:
	uv run ruff check brain_games

test:
	uv run pytest

cov:
	uv run pytest --cov=brain_games --cov-report term-missing

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

docker-package-install:
	uv pip install --system dist/*.whl

package-uninstall:
	uv tool uninstall hexlet-code


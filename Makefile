install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl
	
lint:
	poetry run flake8 brain_games

package-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl

package-uninstall:
	python3 -m pip uninstall hexlet-code

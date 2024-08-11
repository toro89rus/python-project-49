install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-install-venv:
	python3 -m pip install dist/*.whl

package-install-pipx:
	pipx install dist/*.whl
	
lint:
	poetry run flake8 brain_games

package-uninstall:
	python3 -m pip uninstall --user hexlet-code

package-uninstall-venv:
	python3 -m pip uninstall hexlet-code

package-uninstall-pipx:
	pipx uninstall hexlet-code
	


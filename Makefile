format:
	black .
	isort . --skip-gitignore
	flake8 . --exclude .venv --format=pylint
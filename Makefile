install:
	pip install -r requirements.txt

install_dev:
	pip install -r requirements-dev.txt && pre-commit install

run:
	python src/main.py
create_venv:
	python3 -m venv venv

clean_venv:
	rm -rf venv

install_requirements:
	. venv/bin/activate && pip install -r requirements.txt

install_dev_requirements:
	. venv/bin/activate && pip install -r requirements-dev.txt

install_pre_commit:
	. venv/bin/activate && pre-commit install

setup:
	make create_venv && make install_requirements && make install_dev_requirements && make install_pre_commit

test:
	. venv/bin/activate && pytest -v --cov --cov-fail-under=80 --cov-report=term

run:
	. venv/bin/activate && python src/main.py

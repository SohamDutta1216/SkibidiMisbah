default:
	@make run

run:
	python3 main.py

web:
	python3 -m pygbag main.py

web-build:
	python3 -m pygbag --build main.py

web-dev:
	python3 -m pygbag main.py

init:
	@python3 -m pip install -U pip; \
	python3 -m pip install -r requirements.txt; \
	python3 -m pip install pygbag; \
	pre-commit install;

clean:
	rm -rf build/
	rm -rf __pycache__/
	rm -rf *.pyc

pre-commit:
	pre-commit install

pre-commit-all:
	pre-commit run --all-files

format:
	black .

lint:
	flake8 --config=../.flake8 --output-file=./coverage/flake8-report --format=default

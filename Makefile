install:
	python -m pip install --upgrade pip &&\
	python -m pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:
	black *.py

lint:
	pylint --disable=R,C str_counter.py

all: install lint test
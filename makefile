VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

run: test
	$(PYTHON) main.py

test: $(VENV)/bin/activate
	$(PIP) install coverage
	coverage run test_main.py

$(VENV)/bin/activate: requirements.txt
	python -m venv $(VENV)
	$(PIP) install -r requirements.txt


clean:
	rm -rf __pycache__
	rm -rf $(VENV)
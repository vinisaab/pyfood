install:
	pip install -e .['dev']

clean:
	pip uninstall pyfood

test:
	pytest tests/ -v
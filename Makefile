

.PHONY: install

run:
	source ve/bin/activate && python -mapp

install:
	virtualenv ve
	source ve/bin/activate && pip install -r requirements.txt


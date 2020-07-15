pysimplegui/README.md: pysimplegui/PySimpleGui.ipynb
	./jupyternb2markdown.sh pysimplegui/PySimpleGui.ipynb
	mv pysimplegui/PySimpleGui.md pysimplegui/README.md

mqtt/README.md: mqtt/mqtt.ipynb
	./jupyternb2markdown.sh mqtt/mqtt.ipynb
	mv mqtt/mqtt.md mqtt/README.md

venv: */requirements.txt requirements.txt
	python3 -m venv venv
	touch venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -r requirements.txt
	./init_venv.sh

test: venv
	venv/bin/python run_tests.py
	
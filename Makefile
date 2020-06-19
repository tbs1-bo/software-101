pysimplegui/README.md: pysimplegui/PySimpleGui.ipynb
	./export.sh pysimplegui/PySimpleGui.ipynb
	mv pysimplegui/PySimpleGui.md pysimplegui/README.md

mqtt/README.md: mqtt/mqtt.ipynb
	./export.sh mqtt/mqtt.ipynb
	mv mqtt/mqtt.md mqtt/README.md

venv: */requirements.txt
	python3 -m venv venv
	touch venv
	venv/bin/pip install --upgrade pip
	./init_venv.sh

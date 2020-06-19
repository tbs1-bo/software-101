pysimplegui/README.md: pysimplegui/PySimpleGui.ipynb
	./export.sh pysimplegui/PySimpleGui.ipynb
	mv pysimplegui/PySimpleGui.md pysimplegui/README.md

venv: */requirements.txt
	python3 -m venv venv
	touch venv
	venv/bin/pip install --upgrade pip
	./init_venv.sh

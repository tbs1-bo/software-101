flask/flask_final.html: flask/flask.ipynb
	cd flask ; ./process_notebook.sh
	jupyter nbconvert --to html --stdout flask/flask_final.ipynb > flask/flask_final.html
	rm flask/flask_final.ipynb

datenbank/README.md: datenbank/datenbank.ipynb
	./jupyternb2markdown.sh datenbank/datenbank.ipynb datenbank/README.md

bottle/README.md: bottle/bottle.ipynb
	./jupyternb2markdown.sh bottle/bottle.ipynb bottle/README.md

pygame-zero/README.md: pygame-zero/pgzero_demo.ipynb
	./jupyternb2markdown.sh pygame-zero/pgzero_demo.ipynb pygame-zero/pgzero_demo.md pygame-zero/README.md

pysimplegui/README.md: pysimplegui/PySimpleGui.ipynb
	./jupyternb2markdown.sh pysimplegui/PySimpleGui.ipynb pysimplegui/PySimpleGui.md pysimplegui/README.md

dotenv/README.md: dotenv/dotenv.ipynb
	./jupyternb2markdown.sh dotenv/dotenv.ipynb dotenv/README.md

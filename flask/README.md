## Installation


```python
# testing audio
from IPython.display import Audio
Audio(url="http://www.w3schools.com/html/horse.ogg")
```





<audio  controls="controls" >
    <source src="http://www.w3schools.com/html/horse.ogg" type="audio/ogg" />
    Your browser does not support the audio element.
</audio>





```python
pip install flask
```


```python
%%writefile app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Meine TODO-App'

app.run()
```

    Overwriting app.py


## Starten

    $ FLASK_ENV=development FLASK_APP=app.py flask run
    
Windows:

    set FLASK_APP=app.py
    set FLASK_ENV=development
    flask run
    

http://localhost:5000/


```python
%%writefile app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
      <head>
      <title>Todo App</title>
    </head>
    <body>
      <h1>Todo App</h1>
    </body>
    </html>
    '''
```

    Overwriting app.py


Änderungen zur vorherigen Version sind im Folgenden mit `#` markiert.

## Templates


```python
! mkdir templates
```

    mkdir: das Verzeichnis „templates“ kann nicht angelegt werden: Die Datei existiert bereits



```python
%%writefile templates/index.html

<!DOCTYPE html>
<html>
  <head>
  <title>Todo App</title>
</head>
<body>
  <h1>Todo App</h1>
</body>
</html>
```

    Overwriting templates/index.html



```python
%%writefile app.py

from flask import Flask, render_template  #

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  #
```

    Overwriting app.py


## Templates Mit Parametern


```python
%%writefile templates/index.html

<!DOCTYPE html>
<html>
  <head>
  <title>Todo App</title>
</head>
<body>
  <h1>Todo App</h1>

    <!-- Ausdrücke werden in doppelte geschweifte Klammern gesetzt -->
    {{ tasks }}

</body>
</html>
```

    Overwriting templates/index.html



```python
%%writefile app.py

from flask import Flask, render_template

app = Flask(__name__)
my_tasks = ['Learn Flask', 'Make App']  #

@app.route('/')
def index():
    return render_template('index.html',tasks=my_tasks)  #
```

    Overwriting app.py


## Schleifen in Templates


```python
%%writefile templates/index.html

<!DOCTYPE html>
<html>
  <head>
  <title>Todo App</title>
</head>
<body>
    <h1>Todo App</h1>
    <ul>

    <!-- for-Schleifen in Templates -->
    {% for task in tasks %}
    <li> {{ task }} </li>
    {% endfor%}

    </ul>
</body>
</html>
```

    Overwriting templates/index.html


## Formulare


```python
%%writefile templates/index.html

<!DOCTYPE html>
<html>
  <head>
  <title>Todo App</title>
</head>
<body>
    <h1>Todo App</h1>
    <ul>
    {% for task in tasks %}
    <li> {{ task }} </li>
    {% endfor %}
    </ul>
    
    <!-- Formular -->
    <h2>Task hinzufügen</h2>
    <form action='' method='post'>
        <label for='content'>Inhalt:</label>
        <input type='text' name='content' placeholder="Neuer Task">
        <input type='submit' value='Add'>
    </form>
</body>
</html>
```

    Overwriting templates/index.html



```python
%%writefile app.py

from flask import Flask, render_template, request, redirect #

app = Flask(__name__)

my_tasks = ['Learn Flask', 'Make App']

@app.route('/', methods=['GET', 'POST'])    #
def index():
    if request.method == 'POST':            #
        new_task = request.form['content']  #
        my_tasks.append(new_task)           #
        return redirect('/')                #
    else:
        return render_template('index.html',tasks=my_tasks)
```

    Overwriting app.py


## Daten speichern


```python
pip install flask-sqlalchemy
```


```python
%%writefile app.py

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy, Model   #

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  #
db = SQLAlchemy(app)  #

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_task = request.form['content']
        t = Task(content=new_task)  #
        db.session.add(t)           #
        db.session.commit()         #
        return redirect('/')
    else:
        my_tasks = Task.query.all() #
        return render_template('index.html',tasks=my_tasks)
    

class Task(db.Model):                             #
    id = db.Column(db.Integer, primary_key=True)  #
    content = db.Column(db.String(128))           #
    
db.create_all()                                   #
```

    Overwriting app.py



```python
%%writefile templates/index.html

<!DOCTYPE html>
<html>
  <head>
  <title>Todo App</title>
</head>
<body>
    <h1>Todo App</h1>
    <ul>
    {% for task in tasks %}
    <li> {{ task.content }} </li>  <!-- Nun kann auf den Content des Objektes zugegriffen werden -->
    {% endfor %}
    </ul>
    
    <h2>Task hinzufügen</h2>
    <form action='' method='post'>
        <label for='content'>Inhalt:</label>
        <input type='text' name='content' placeholder="Neuer Task">
        <input type='submit' value='Add'>
    </form>
</body>
</html>
```

    Overwriting templates/index.html


## Daten löschen


```python
%%writefile app.py

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy, Model

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_task = request.form['content']
        t = Task(content=new_task)
        db.session.add(t) 
        db.session.commit() 
        return redirect('/')
    else:
        my_tasks = Task.query.all()
        return render_template('index.html',tasks=my_tasks)

@app.route('/delete/<int:id>')  #
def delete(id):                 #
    t = Task.query.get(id)      #
    db.session.delete(t)        #
    db.session.commit()         #
    return redirect('/')        #
    
# models
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(128))
    
db.create_all()
```

    Overwriting app.py



```python
%%writefile templates/index.html

<!DOCTYPE html>
<html>
  <head>
  <title>Todo App</title>
</head>
<body>
    <h1>Todo App</h1>
    <ul>
    {% for task in tasks %}

    <li> {{ task.content }} 
        <!-- Löschlink: über url_for() wird die Route für eine Methode ermittelt. -->
        <a href='{{url_for("delete", id=task.id)}}'>DEL</a> 
    </li>

    {% endfor %}
    </ul>
    
    <h2>Task hinzufügen</h2>
    <form action='' method='post'>
        <label for='content'>Inhalt:</label>
        <input type='text' name='content' placeholder="Neuer Task">
        <input type='submit' value='Add'>
    </form>
</body>
</html>
```

    Overwriting templates/index.html


## Schickes Layout

https://watercss.kognise.dev/

CSS herunterladen https://cdn.jsdelivr.net/npm/water.css@2/out/water.css


```python
! mkdir static
```


```python
! wget -O static/water.css https://cdn.jsdelivr.net/npm/water.css@2/out/water.css
```


```python
%%writefile templates/index.html

<!DOCTYPE html>
<html>
  <head>
    <!-- Stylesheet -->
    <link rel="stylesheet" href="{{url_for('static', filename='water.css')}}">   
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>Todo App</title>
</head>
<body>
    <h1>Todo App</h1>
    <ul>
    {% for task in tasks %}
    <li> {{ task.content }} <a href='{{url_for("delete", id=task.id)}}'>DEL</a> </li>
    {% endfor %}
    </ul>
    
    <h2>Task hinzufügen</h2>
    <form action='' method='post'>
        <label for='content'>Inhalt:</label>
        <input type='text' name='content' placeholder="Neuer Task">
        <input type='submit' value='Add'>
    </form>
</body>
</html>
```

    Overwriting templates/index.html



```python

```

## Installation

Unten siehst du Steuerelemente, um eine Erläuterung abzuspielen. Setze Kopfhörer auf und höre dir die Erläuterungen zu den jeweiligen Abschnitten an.


<audio controls>
  <source src="https://archive.org/download/flask_intro/installation.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio> 



```python
pip3 install flask
```

[flask-Webseite](https://flask.palletsprojects.com)


```python
flask --version
```

    Python 3.9.5
    Flask 1.1.2
    Werkzeug 1.0.1



```python
flask
```

    Usage: flask [OPTIONS] COMMAND [ARGS]...
    
      A general utility script for Flask applications.
    
      Provides commands from Flask, extensions, and the application. Loads the
      application defined in the FLASK_APP environment variable, or from a
      wsgi.py file. Setting the FLASK_ENV environment variable to 'development'
      will enable debug mode.
    
        $ export FLASK_APP=hello.py
        $ export FLASK_ENV=development
        $ flask run
    
    Options:
      --version  Show the flask version
      --help     Show this message and exit.
    
    Commands:
      routes  Show the routes for the app.
      run     Run a development server.
      shell   Run a shell in the app context.



```python
flask run --help
```

    Usage: flask run [OPTIONS]
    
      Run a local development server.
    
      This server is for development purposes only. It does not provide the
      stability, security, or performance of production WSGI servers.
    
      The reloader and debugger are enabled by default if FLASK_ENV=development
      or FLASK_DEBUG=1.
    
    Options:
      -h, --host TEXT                 The interface to bind to.
      -p, --port INTEGER              The port to bind to.
      --cert PATH                     Specify a certificate file to use HTTPS.
      --key FILE                      The key file to use when specifying a
                                      certificate.
    
      --reload / --no-reload          Enable or disable the reloader. By default
                                      the reloader is active if debug is enabled.
    
      --debugger / --no-debugger      Enable or disable the debugger. By default
                                      the debugger is active if debug is enabled.
    
      --eager-loading / --lazy-loader
                                      Enable or disable eager loading. By default
                                      eager loading is enabled if the reloader is
                                      disabled.
    
      --with-threads / --without-threads
                                      Enable or disable multithreading.
      --extra-files PATH              Extra files that trigger a reload on change.
                                      Multiple paths are separated by ':'.
    
      --help                          Show this message and exit.



<audio controls>
  <source src="https://archive.org/download/flask_intro/einfache_app.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>



```python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Meine TODO-App'
```

Probiere es nun selbst aus: Installiere flask, erstelle die Dateien und starte den 
Web-Server. Lasse ihn die ganze Zeit im Hintergrund laufen und beobachte, welche 
Ausgaben er produziert.

## Web-Server starten


<audio controls>
  <source src="https://archive.org/download/flask_intro/flask_starten.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>


MacOS/Linux:

    export FLASK_APP=app.py
    export FLASK_ENV=development
    flask run
    
Windows:

    set FLASK_APP=app.py
    set FLASK_ENV=development
    flask run
    

[http://localhost:5000/](http://localhost:5000/)

## HTML-Ausgabe


<audio controls>
  <source src="https://archive.org/download/flask_intro/return_html.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio> 



```python

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

Änderungen zur vorherigen Version sind im Folgenden mit `#` markiert.

## Templates


<audio controls>
  <source src="https://archive.org/download/flask_intro/render_template.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio> 



```python
mkdir templates
```


```python
tree templates
```

    templates
    └── index.html
    
    0 directories, 1 file



```python

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

<!DOCTYPE html>
<html>
<head>
  <title>Todo App</title>
</head>
<body>
  <h1>Todo App</h1>
</body>
</html>


```python

from flask import Flask, render_template  #

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  #
```

[Rendering Template](https://flask.palletsprojects.com/en/2.0.x/quickstart/#rendering-templates)

## Templates mit Parametern


<audio controls>
  <source src="https://archive.org/download/flask_intro/templates_param.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio> 



```python

<!DOCTYPE html>
<html>
<head>
  <title>Todo App</title>
</head>
<body>
  <h1>Todo App</h1>

    <!-- # Ausdrücke werden in doppelte geschweifte Klammern gesetzt -->
    {{ tasks }}

</body>
</html>
```


```python

from flask import Flask, render_template

app = Flask(__name__)
my_tasks = ['Learn Flask', 'Make App']                    #

@app.route('/')
def index():
    return render_template('index.html', tasks=my_tasks)  #
```

## Schleifen in Templates


<audio controls>
  <source src="https://archive.org/download/flask_intro/template_loop.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio> 



```python

<!DOCTYPE html>
<html>
<head>
  <title>Todo App</title>
</head>
<body>
    <h1>Todo App</h1>
    <ul>

        <!-- # for-Schleifen in Templates -->
        {% for task in tasks %}
            <li> {{ task }} </li>
        {% endfor %}

    </ul>
</body>
</html>
```

<h1>Todo App</h1>
<ul>
    <li> Learn Flask </li>
    <li> Make App </li>
</ul>

## Formulare


<audio controls>
  <source src="https://archive.org/download/flask_intro/html_form.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio> 



```python

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
    
    <!-- # Formular -->
    <h2>Task hinzufügen</h2>
    <form action='' method='post'>
        <label for='content'>Inhalt:</label>
        <input type='text' name='content' placeholder="Neuer Task">
        <input type='submit' value='Add'>
    </form>

</body>
</html>
```

<h2>Task hinzufügen</h2>
<form action='' method='post'>
    <label for='content'>Inhalt:</label>
    <input type='text' name='content' placeholder="Neuer Task">
    <input type='submit' value='Add'>
</form>


<audio controls>
  <source src="https://archive.org/download/flask_intro/http_post_processing.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio> 



```python

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
        return render_template('index.html', tasks=my_tasks)
```

[Accessing Request Data](https://flask.palletsprojects.com/en/2.0.x/quickstart/#accessing-request-data)

## Daten in einer Datenbank speichern


<audio controls>
  <source src="https://archive.org/download/flask_intro/sql_alchemy.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio> 



```python
pip install flask-sqlalchemy
```


```python

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy, Model                #

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'  #
db = SQLAlchemy(app)                                          #

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
        return render_template('index.html', tasks=my_tasks)
    

class Task(db.Model):                             #
    id = db.Column(db.Integer, primary_key=True)  #
    content = db.Column(db.String(128))           #
    
db.create_all()                                   #
```


```python

<!DOCTYPE html>
<html>
<head>
  <title>Todo App</title>
</head>
<body>
    <h1>Todo App</h1>
    <ul>
    {% for task in tasks %}
        <!-- # Nun kann auf den Content des Objektes zugegriffen werden -->
        <li> {{ task.content }} </li>  
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

[Flask-SQL-Alchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/)

## Daten löschen


<audio controls>
  <source src="https://archive.org/download/flask_intro/delete.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio> 



```python

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
        return render_template('index.html', tasks=my_tasks)

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


```python

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
        <!-- # Löschlink: über url_for() wird die Route für eine Methode ermittelt. -->
        <a href='{{url_for("delete", id=task.id)}}'>DELETE</a> 
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

<h1>Todo App</h1>
<ul>
<li> Learn Flask 
    <a href='/delete/1'>DELETE</a> 
</li>
<li> Make App 
    <a href='/delete/2'>DELETE</a> 
</li>

----
- [URL Building](https://flask.palletsprojects.com/en/2.0.x/quickstart/#url-building)

## Schickes Layout

[Water CSS](https://watercss.kognise.dev/)

CSS herunterladen https://cdn.jsdelivr.net/npm/water.css@2/out/water.css


<audio controls>
  <source src="https://archive.org/download/flask_intro/stylesheet.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio> 



```python
mkdir static
wget -O static/water.css https://cdn.jsdelivr.net/npm/water.css@2/out/water.css
```


```python
tree static
```

    static
    └── water.css
    
    0 directories, 1 file



```python

<!DOCTYPE html>
<html>
<head>
    <!-- # Stylesheet -->
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

## Daten ändern


<audio controls>
  <source src="https://archive.org/download/flask_intro/update.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio> 



```python
tree templates
```

    templates
    ├── index.html
    └── update.html
    
    0 directories, 2 files



```python

<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{{url_for('static', filename='water.css')}}">   
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Todo App</title>
</head>
<body>
    <h1>Todo App</h1>
    <ul>
    {% for task in tasks %}

    <li> {{ task.content }} 
        <a href='{{url_for("delete", id=task.id)}}'>DELETE</a> 

        <!-- # Updatelink ergänzt -->
        <a href='{{url_for("update", id=task.id)}}'>UPDATE</a> 

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

<h1>Todo App</h1>
<ul>
<li> Learn Flask 
    <a href='/delete/1'>DELETE</a> 
    <a href='/update/1'>UPDATE</a> 
</li>
<li> Make App 
    <a href='/delete/2'>DELETE</a> 
    <a href='/update/2'>UPDATE</a> 
</li>


```python

<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{{url_for('static', filename='water.css')}}">   
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Todo App</title>
</head>
<body>
    <h2>Task Ändern</h2>
    <form action='{{ url_for("update", id=task.id) }}' method='post'>
        <label for='content'>Inhalt:</label>
        <input type='text' name='content' value="{{ task.content }}">
        <input type='submit' value='Update'>
    </form>
</body>
</html>
```

<h2>Task Ändern</h2>
<form action='/update/1' method='post'>
    <label for='content'>Inhalt:</label>
    <input type='text' name='content' value="Learn Flask">
    <input type='submit' value='Update'>
</form>


```python

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
        return render_template('index.html', tasks=my_tasks)

@app.route('/delete/<int:id>')
def delete(id):                 
    t = Task.query.get(id)      
    db.session.delete(t)        
    db.session.commit()         
    return redirect('/')        
    
@app.route('/update/<int:id>', methods=['GET', 'POST'])  #
def update(id):                                          #
    t = Task.query.get(id)                               #
    if request.method == 'POST':                         #
        t.content = request.form['content']              #
        db.session.commit()                              # 
        return redirect('/')                             #
    else:                                                #
        return render_template('update.html', task=t)    #

# models
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(128))
    
db.create_all()
```

## Quiz

- [Quiz](https://forms.office.com/Pages/ResponsePage.aspx?id=vXaNqv_gIkSSC8VeqJUdRS_J0kTXn4pIneR-vyqBhblUQkgyVjFMRE1GMjlKNDAxNTAwSDVaQjAzTS4u) - Office-Zugang erforderlich

## Weitere Infos

* [Quickstart](https://flask.palletsprojects.com/en/2.0.x/quickstart/)

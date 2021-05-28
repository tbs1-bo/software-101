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




<audio controls>
  <source src="https://www.w3schools.com/html/horse.ogg" type="audio/ogg">
  <source src="http://www.w3schools.com/html/horse.mp3" type="audio/mpeg">
Your browser does not support the audio element.
</audio> 


```python
pip3 install flask
```


```python
! flask
```

    /home/pintman/.local/lib/python3.9/site-packages/flask_sqlalchemy/__init__.py:872: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
      warnings.warn(FSADeprecationWarning(
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
! flask run --help
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



```python
%%writefile app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Meine TODO-App'
```

    Overwriting app.py


## Starten

MacOS/Linux:

    export FLASK_ENV=development
    export FLASK_APP=app.py
    flask run
    
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

    <!-- # Ausdrücke werden in doppelte geschweifte Klammern gesetzt -->
    {{ tasks }}

</body>
</html>
```

    Overwriting templates/index.html



```python
%%writefile app.py

from flask import Flask, render_template

app = Flask(__name__)
my_tasks = ['Learn Flask', 'Make App']                   #

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

    <!-- # for-Schleifen in Templates -->
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


## Daten in einer Datenbank speichern


```python
pip install flask-sqlalchemy
```


```python
%%writefile app.py

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

    Overwriting templates/index.html


## Schickes Layout

https://watercss.kognise.dev/

CSS herunterladen https://cdn.jsdelivr.net/npm/water.css@2/out/water.css


```python
! mkdir static
! wget -O static/water.css https://cdn.jsdelivr.net/npm/water.css@2/out/water.css
```


```python
! ls static
```

    water.css



```python
%%writefile templates/index.html

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

    Overwriting templates/index.html


## Daten ändern


```python
%%writefile templates/index.html

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

    Overwriting templates/index.html



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

@app.route('/delete/<int:id>')
def delete(id):                 
    t = Task.query.get(id)      
    db.session.delete(t)        
    db.session.commit()         
    return redirect('/')        
    
@app.route('/update/<int:id>', methods=['GET', 'POST'])  #
def update(id):                                          #
    t = Task.query.get(id)
    if request.method == 'POST':
        t.content = request.form['content']
        db.session.commit()
        return redirect('/')
    else:
        return render_template('update.html', task=t)
    
# models
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(128))
    
db.create_all()
```

    Overwriting app.py



```python
%%writefile templates/update.html

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

    Overwriting templates/update.html


## Weitere Infos

* [Quickstart](https://flask.palletsprojects.com/en/2.0.x/quickstart/)

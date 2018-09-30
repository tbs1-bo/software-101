
# Pygame Zero

## Installation 

[Pygame Zero](http://pygame-zero.readthedocs.io) ist eine auf 
pygame aufbauende Bibliothek. Sie kann 
leicht mit pip installiert werden.

    $ pip install pgzero
    
Danach steht das Kommandozeilentool `pgzrun` zur 
Verfügung, mit dem
die Python-Dateien gestartet werden können. 

## Ein leeres Fenster

Eine leere Datei ist bereits ein Programm für PyGameZero. Man kann zusätzlich die Dimensionen des Fensters eingeben. 


```python
# demo.py
WIDTH = 300
HEIGHT = 300
```



Die Datei `demo.py` kann nun mit `pgzrun` ausgeführt werden.


```python
pgzrun demo.py
```

    pygame 1.9.4
    Hello from the pygame community. https://www.pygame.org/contribute.html


## Start ohne pgzrun

Alternativ kann ein Programm auch direkt über Python gestartet werden. Dazu muss das Modul `pgzrun` importiert und am Ende des Programms aufgerufen werden.


```python

import pgzrun

WIDTH = 300
HEIGHT = 300

# run main gameloop
pgzrun.go()
```




```python
python3 demo.py
```

    pygame 1.9.4
    Hello from the pygame community. https://www.pygame.org/contribute.html


## Gameloop

Eine gameloop einer Spiele-Engine ist nach dem folgenden Muster aufgebaut.

    while game_has_not_ended():
        process_input()
        update()
        draw()

Und genau so funktioniert auch die Gameloop bei Pygame-Zero: Zunächst werden die Eingaben verarbeitet (`process_input`), dann die Spielwelt aktualisiert (`update`) und schließlich die veränderte Spielwelt gezeichnet (`draw`). Das passiert ca. 60 mal in der Sekunde.

## Bilder

Ein Verzeichnis `images` enthält Bilder, die automatisch geladen werden.


```python
file images/*
```

    images/ball.gif: GIF image data, version 89a, 111 x 111


Nun wird ein Objekt von der Klasse *Actor* erstellt und mit einem Bild initialisiert. Jeder Actor hat eine Position (.x und .y), die nun in jedem Frame 60 mal pro Sekunde mit der Funktion `update` geändert wird. Danach wird die Methode `draw` aufgerufen, die die Spielwelt zeichnet.


```python

ball = Actor("ball")  # create actor

def update():
    ball.x += 1  # move actor
    
def draw():
    ball.draw()  # draw actor 
```




```python
pgzrun demo.py
```

    pygame 1.9.4
    Hello from the pygame community. https://www.pygame.org/contribute.html


Es entsteht ein unschöner "Ball-Streifen". Um dies zu vermeiden, muss der Hintergrund zuvor immer gelöscht werden.


```python

ball = Actor("ball")

def update():
    ball.x += 1

def draw():
    screen.fill((0,0,0))  # clear the screen
    ball.draw()
```




```python
pgzrun demo.py
```

    pygame 1.9.4
    Hello from the pygame community. https://www.pygame.org/contribute.html


## Interaktion mit der Maus

Schließlich können wir auch auf Mouseclicks reagieren. Dafür muss eine Methode `on_mouse_down` erstellt werden, die aufgerufen wird, sobald die Maus geklickt wird.


```python

ball = Actor("ball")
direction = 1

def update():
    ball.x += direction

def draw():
    screen.fill((0,0,0))
    ball.draw()
    
def on_mouse_down(pos):  # handle mouse clicks
    global direction
    direction *= -1 # change direction on mouseclick
```




```python
pgzrun demo.py
```

    pygame 1.9.4
    Hello from the pygame community. https://www.pygame.org/contribute.html


## Sound

Sounds werde so ähnlich wie Bilder gehandhabt. Es muss ein Verzeichnis `sounds` existieren, in dem sich die Sounddateien (als WAV) befinden.


```python

def on_mouse_down(pos):
    sounds.punch.play()  # play sounds/punch.wav
```



Der Sound [sounds/punch.wav](sounds/punch.wav) wird nun bei jedem Klick abgespielt.


```python
pgzrun demo.py
```

    pygame 1.9.4
    Hello from the pygame community. https://www.pygame.org/contribute.html


## Objekt-Orientierte Bälle

Nun soll das Programm objekt-orientiert mit einer Klasse umgesetzt werden. Das ermöglicht es uns, mit mehreren Bällen unabhängig umgehen zu können.


```python

class Ball:  # Eine Klasse Ball mit verschiedenen Methoden
    def __init__(self, x, y):
        self.act = Actor("ball")
        self.act.x = x
        self.act.y = y
        self.direction = 1

    def draw(self):
        self.act.draw()
        
    def update(self):
        self.act.x += self.direction
        
    def clicked(self):
        self.direction *= -1
```



Wir erstellen ein paar Ball-Objekte und ergänzen Event-Methoden für die Bälle.


```python

# creating some balls
balls = [Ball(0, 60), Ball(30, 180), Ball(60, 250)]

# event methods for all balls
def draw():
    screen.fill((0,0,0))
    for ball in balls: 
        ball.draw()
    
def update():
    for ball in balls:
        ball.update()
    
def on_mouse_down(pos):
    for ball in balls:
        ball.clicked()
```




```python
pgzrun demo.py
```

    pygame 1.9.4
    Hello from the pygame community. https://www.pygame.org/contribute.html


## Support für den Mu-Editor

Der Editor [Mu](https://codewith.mu/) besitzt einen eigenen Modus für
Pygame-Zero-Spiele.

## Weitere Informationen

Ein [Cheat Sheet](pygame-zero-cheatsheet.pdf) fasst die wichtigsten Aspekte zusammen.

Die beim Aufruf mit `pgzrun` verfügbaren Objekte sind in der Dokumentation im Abschnitt
[builtins](http://pygame-zero.readthedocs.io/en/stable/builtins.html) beschrieben.

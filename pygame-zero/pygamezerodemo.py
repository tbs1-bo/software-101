# Es werden keine Imports benötigt. Dafür muss die Datei mit
# 'pgzrun pygamezerodemo.py' aufgerufen werden.
#
# Dadurch werden einige globale Variablen und Klassen verfügbar gemacht: 
# screen, actor, Actor und weitere:
# http://pygame-zero.readthedocs.io/en/stable/builtins.html

# Titel des Fensters
TITLE = "Pygame Zero Demo"

# Dimensionen des Fensters
WIDTH = 400
HEIGHT = 300

class Ball():
    def __init__(self):
        # erzeugt einen Actor. Als Bild wird eine Datei 'images/ball.gif'
        # erwartet. Andere Dateiendungen sind möglich.
        self.actor = Actor("ball", (150,150))

        self.speed = [2, 2]  # Geschwindigkeit in x- und y-Richtung

    def update(self):
        ball.actor.x += self.speed[0]
        ball.actor.y += self.speed[1]

        # Richtung des Balles ändern, wenn der Rand berührt wird
        if self.actor.left < 0 or self.actor.right > WIDTH:
            self.bounce(xdir=True, ydir=False)
        if self.actor.top < 0 or self.actor.bottom > HEIGHT:
            self.bounce(xdir=False, ydir=True)

    def bounce(self, xdir=True, ydir=False):
        """Kehre die X- oder Y-Richtung des Balles um."""
        if xdir:
            self.speed[0] *= -1
        if ydir:
            self.speed[1] *= -1

def update():
    """Update-Funktion, die für jeden Frame 60 mal pro Sekunde einmal 
    aufgerufen wird. Hier wird die Spielwelt aktualisiert aber noch nichts
    gezeichnet."""
    ball.update()

def draw():
    """Draw-Funktion, die nach dem Update den Bildschirm zeichnet."""
    screen.fill((128,0,0))
    ball.actor.draw()

def on_mouse_down(pos):
    """Eine von verschiedenen Event-Funktionen. Sie wird bei einem
    Mouseclick aufgerufen. Beim Aufruf wird die Position der Mouse
    als Parameter übergeben."""

    if ball.actor.collidepoint(pos):
        ball.bounce()



ball = Ball()

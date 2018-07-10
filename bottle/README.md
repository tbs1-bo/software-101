# Bottle

[Bottle](https://bottlepy.org) ist ein Webframework, das leicht mit pip
installiert werden kann.

    $ pip install bottle

Das Demoprogramm [bottledemo.py](bottledemo.py) zeigt eine Webseite mit einem
[Bild](ball.gif) und einer Zahl, die sich bei jedem Refresh durch den Browser
ändert. Für
jeden Pfad, der aufgerufen werden kann, muss eine Route in Bottle deklariert
werden. Diese Methode muss einfaches HTML an den Browser liefern. Für Dateien
muss eine separate Route deklariert werden, die Dateien und kein HTML
ausliefert.

import bottle
import time


@bottle.route("/")  # bindung route to a method
def index():
    t = time.time()
    html = """
        <!DOCTYPE html>
        <html>
          <head><title>Bottle Demo</title></head>
          <body>
            <h1>Bottle-Demo</h1>
            <img src="/image/ball.gif" />
            <p>
            {sekseit1970} Sekunden seit dem 1.1.1970. 
            <p/>
          </body>
        </html>
        """

    # return HTML but replace variable in string before
    return html.format(sekseit1970=t)


@bottle.route("/image/<dateiname>")  # dynamic route
def image(dateiname):
    """Serve static files."""
    return bottle.static_file(filename=dateiname, root=".")


if __name__ == "__main__":
    bottle.run(host="127.0.0.1", port=8081, reloader=True)

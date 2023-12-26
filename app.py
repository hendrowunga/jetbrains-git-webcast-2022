import flask

app= flask.Flask(__name__)

@app.get('/')
def index():
    return "Hallo world"



















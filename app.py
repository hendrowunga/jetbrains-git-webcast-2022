import flask

app= flask.Flask(__name__)

@app.get('/')
def index():
    return "Hallo world"
@app.get('/about')
def about():
    return ("Thi is a demo app,it's simple")



















import flask

__VERSION__ = '0.0.1'
app= flask.Flask(__name__)



print('App starting up ,version{__VERSION__}')
@app.get('/')
def index():
    return flask.render_template('index.html')
@app.get('/about')
def about():
    return ("Thi is a demo app,it's simple")



















from flask import Flask, render_template, request
from graph import Graph


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', url=' ')


@app.route('/select_graph/', methods=['POST'])
def hello():
    g = Graph()
    result = request.form['graph']
    if result == 'Happy':
        img = g.music_happy
    else:
        img = g.music_lonely
    return render_template("home.html", url=img)


''' 
4. Compléter le README
5. Compléter notebook 
'''

import io

from flask import Flask, render_template, request
from graph import Graph

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('formulaire.html')


@app.route('/home', methods=['POST'])
def resultat():
    result = request.form
    d = result['music']
    return render_template("home.html", music=d)


@app.route('/hello/')
def hello():
    g = Graph()
    img = g.music_on_loneliness

    return render_template("plot.html", url=img)


''' 
1. Créer des sélecteurs > template 'jinja' et des formulaires 
2. routes avec des requêtes POST pour récupérer les infos sélectionnés 
3. Display les graphiques en fonction des sélecteurs.
    1. Créer les graphiques
    2. Sauvegarder les graphiques sur local
    3. Display graphique as IMG 


4. Compléter le README
5. Compléter notebook 
'''

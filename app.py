from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

# Page d'accueil (formulaire)
@app.route('/')
def home():
    return render_template("form.html")

# Traitement des données du formulaire
@app.route('/submit', methods=['POST'])
def submit():
    nom = request.form['nom']
    age = request.form['age']
    sexe = request.form['sexe']
    ville = request.form['ville']
    secteur = request.form['secteur']

    # Sauvegarde dans un fichier CSV
    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([nom, age, sexe, ville, secteur])

    return """
    <h2>Données enregistrées avec succès ✅</h2>
    <a href="/">Retour au formulaire</a>
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    
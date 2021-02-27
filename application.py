from flask import Flask
#primo semplice programma utilizzando FLASK in modalità virtuasle con ENV
app = Flask(__name__)
#creazione pagina home
@app.route("/")
def homepage():
    return "<h1 style='color:red'>Nuovo titolo</h1>"

#utilizzo decoratori per collegamento pagine
@app.route("/contatti")
def contatti():
    return "<span style='color:grey'>Contattaci!</span>"

@app.route("/chi-siamo")
def chi_siamo():
    return "Chi siamo?"

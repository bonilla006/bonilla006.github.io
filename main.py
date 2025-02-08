from flask import Flask, render_template

app = Flask(__name__)

@app.route('/frente_casa/')
def casa():
    return render_template('index.html')

@app.route('/dentro_casa/')
def encasa():
    return render_template('encasa.html')

@app.route('/mesa/')
def mesa():
    return render_template('mesa.html')

@app.route('/carta/')
def carta():
    return render_template('carta.html')

@app.route('/aventura/')
def espacio():
    return render_template('espacio.html')

@app.route('/triste/')
def espacio_triste():
    return render_template('espacio_triste.html')

if __name__ == "__main__":
    app.run(debug=True)

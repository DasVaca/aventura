from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def homepage():
    '''
        Presentación de la página. lo primero que verá el usuario.
    '''

    return render_template('base.html');

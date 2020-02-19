from flask import Flask
from flask import render_template


app = Flask(__name__)
@app.route('/home')
def home():
    event = ['eventoA','eventoB','eventoC']
    return render_template("index.html",eventos=event)
#criei uma rota home que retorna olá mundo
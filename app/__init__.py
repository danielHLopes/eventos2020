from flask import Flask
from flask import render_template


app = Flask(__name__)
@app.route('/home')
def home():
    event = ['eventoA','eventoB','eventoC']
    titulo = "Bem vindo a lista de eventos!"
    return render_template("index.html",eventos=event, titulo = titulo)
#criei uma rota home que retorna olá mundo
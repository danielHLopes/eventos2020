from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
#importando a conexão com o banco
import os

app = Flask(__name__)


db = SQLAlchemy(app)
#crio a instancia com o banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://suporte:$uportE99@localhost/atividades'
#conecxão com o banco
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + '/static/uploads'

from app.models.tables import Usuario
from app.models.tables import Atividade
#importo as tabelas

from app.controllers import atividades

@app.route('/home')
def home():
    usuarios = Usuario.query.all()
    titulo = "Bem vindo a lista de eventos!"
    return render_template("index.html",usuarios=usuarios, titulo = titulo)
#criei uma rota home que retorna olá mundo
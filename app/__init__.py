from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
#importando a conexão com o banco


app = Flask(__name__)


db = SQLAlchemy(app)
#crio a instancia com o banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://suporte:$uportE99@localhost/atividades'
#conecxão com o banco
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app.models.tables import Usuario
from app.models.tables import Atividade
#importo as tabelas


@app.route('/home')
def home():
    usuarios = Usuario.query.all()
    titulo = "Bem vindo a lista de eventos!"
    return render_template("index.html",usuarios=usuarios, titulo = titulo)
#criei uma rota home que retorna olá mundo
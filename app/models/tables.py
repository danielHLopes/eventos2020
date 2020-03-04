from app import db

class Usuario(db.Model):
    #mapeando o banco
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(191), nullable=False)
    email = db.Column(db.String(191), unique=True, nullable=False)
    senha = db.Column(db.String(191), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<Usuario : %>' % self.nome

class Atividade(db.Model):
    #mapeando o banco
    __tablename__ = 'atividades'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(191),nullable=False)
    tipo = db.Column(db.String(191), nullable=False)
    data = db.Column(db.DateTime,nullable=False)
    carga_horaria = db.Column(db.Float,nullable=False)
    arquivo = db.Column(db.String(191),nullable=False)
    usurio_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'),nullable=False)

    def __repr__(self):
        return '<Atividade : %>' % self.nome
    #se eu imprimir a atividade vai vir o nome dela no console

    #para abrir e criar no banco usar python3 para conectar no console depois comando fom app import db e por fim db.create_all()
    #para adicionar um usuario pelo console eu uso from app.models.tables import Usuario depois u1 = usuario(nome="xxx",...) para criar o usuario, db.session.add(u1) e db.session.commit() para mandar para o banco

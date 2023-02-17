from src.db import db

class AlunoModel(db.Model):
    __tablename__ = "alunos"
    
    id = db.Column(db.BigInteger, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.String(120), nullable=False, unique=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.Boolean, default=False)
    data_nascimento = db.Column(db.Date, nullable=False)

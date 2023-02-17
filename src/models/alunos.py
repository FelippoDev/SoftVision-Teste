from src.db import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class AlunoModel(db.Model):
    __tablename__ = "alunos"
    
    id = db.Column(db.BigInteger, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    cpf = db.Column(db.String(120), nullable=False, unique=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.Boolean, default=False)
    data_nascimento = db.Column(db.Date, nullable=False)



# class MatriculaModel(db.Model):
#      id = db.Column(db.Integer, primary_key=True)
#      status = 
#      ano = 
#      alunoId = 
#      cursoId = 
#      dataCadastro = 
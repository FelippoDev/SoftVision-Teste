from src.db import db
from datetime import datetime

class MatriculaModel(db.Model):
    __tablename__ = "matriculas"
    
    id = db.Column(db.BigInteger, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    ano = db.Column(db.String(60), nullable=False)
    aluno = db.Column(db.Integer, db.ForeignKey("alunos.id"))
    curso = db.Column(db.Integer, db.ForeignKey("cursos.id"))
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
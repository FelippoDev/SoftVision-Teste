from src.db import db
from datetime import datetime

class MatriculaModel(db.Model):
     id = db.Column(db.BigInteger, primary_key=True)
     status = db.Column(db.Boolean, default=False)
     ano = db.Column(db.String(60), nullable=False)
     alunoId = db.Column(db.Integer, db.ForeignKey("models.aluno"))
     cursoId = db.Column(db.Integer, db.ForeignKey("models.curso"))
     data_cadastro = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
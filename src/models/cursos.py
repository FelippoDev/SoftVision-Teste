from src.db import db
from datetime import datetime
class CursoModel(db.Model):
    __tablename__ = "cursos"
    
    id = db.Column(db.BigInteger, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    status = db.Column(db.Boolean, default=False)
    slug = db.Column(db.String(180), nullable=False)
    sequencia = db.Column(db.Integer)
    preco_venda = db.Column(db.Float(precision=2), nullable=False)
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    alunos = db.relationship("AlunoModel", back_populates="cursos", secondary="matriculas")
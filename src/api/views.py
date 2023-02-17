from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from . import schemas
from src.models.alunos import AlunoModel
from src.models.cursos import CursoModel
from src.db import db
from marshmallow import ValidationError


class AlunoListView(MethodView):
    schema = schemas.AlunoSchema
    model = AlunoModel
    
    def get(self):
        alunos = self.model.query.all()
        return jsonify(self.schema(many=True).dump(alunos)), 200


class AlunoView(MethodView):    
    schema = schemas.AlunoSchema
    model = AlunoModel
    
    def get(self, id):
        aluno = self.model.query.get_or_404(id)
        aluno = self.schema().dump(aluno)
        return jsonify(aluno)
    
    def post(self):
        data = request.get_json()
        try:
            aluno = self.schema().load(data)
        except ValidationError as error:
            return {"errors": error.messages}, 400
        
        try:
            aluno = self.model(**aluno)
            db.session.add(aluno)
            db.session.commit()
        except IntegrityError as error:
            return {"error": "There already is a aluno with that data."}
        
        return jsonify(self.schema().dump(aluno)), 201
    
    def put(self, id):
        data = request.get_json()
        aluno = self.model.query.get(id)
        if aluno is None:
            return jsonify({'error': 'Aluno não encontrado.'}), 404
        
        aluno.data_nascimento = data['data_nascimento']
        aluno.nome = data['nome']
        aluno.email = data['email']
        aluno.cpf = data['cpf']
        db.session.add(aluno)
        db.session.commit()
        return jsonify(self.schema().dump(aluno)), 201
    
    def delete(self, id):
        aluno = self.model.query.get(id)
        if aluno is None:
            return jsonify({'error': 'Aluno não encontrado.'}), 404
        db.session.delete(aluno)
        db.session.commit()
        return jsonify({'message:': "Aluno deletado com sucesso."}), 202
    



class CursoListView(MethodView):
    schema = schemas.CursoSchema
    model = CursoModel
    
    def get(self):
        cursos = self.model.query.all()
        return jsonify(self.schema(many=True).dump(cursos)), 200
    
    

class CursoView(MethodView):    
    schema = schemas.CursoSchema
    model = CursoModel
    
    def get(self, id):
        curso = self.model.query.get_or_404(id)
        curso = self.schema().dump(curso)
        return jsonify(curso)
    
    def post(self):
        data = request.get_json()
        try:
            curso = self.schema().load(data)
        except ValidationError as error:
            return {"errors": error.messages}, 400
        
        curso['slug'] = curso['nome'].replace(' ','-').lower()
        
        try:
            curso = self.model(**curso)
            db.session.add(curso)
            db.session.commit()
        except IntegrityError as error:
            return {"error": "Já existe um curso com estes dados."}
        
        return jsonify(self.schema().dump(curso)), 201
    
    def put(self, id):
        data = request.get_json()
        curso = self.model.query.get(id)
        if curso is None:
            return jsonify({'error': 'Curso não encontrado.'}), 404
        
        curso.nome = data['nome']
        curso.preco_venda = data['preco_venda']
        curso.sequencia = data['sequencia']
        db.session.add(curso)
        db.session.commit()
        return jsonify(self.schema().dump(curso)), 201
    
    def delete(self, id):
        curso = self.model.query.get(id)
        if curso is None:
            return jsonify({'error': 'Curso não encontrado.'}), 404
        db.session.delete(curso)
        db.session.commit()
        return jsonify({'message:': "Curso deletado com sucesso."}), 202
    
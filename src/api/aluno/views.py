from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from src.api.matricula import schemas
from src.models.alunos import AlunoModel
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
        # aluno = json.loads(aluno)
        # breakpoint()
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
    

from flask import jsonify, request, render_template
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
        """Method for retrieving a specific aluno

        Args:
            id: aluno_id

        Returns:
            A JSON data containing the aluno information
        """
        aluno = self.model.query.get(id)
        if not aluno:
            return jsonify("Aluno not found"), 404
        
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
            if self.model.query.filter_by(email=aluno.email):
                return jsonify("Already is an user with that email."), 400
            if self.model.query.filter_by(email=aluno.cpf):
                jsonify("Already is an user with that CPF."), 400
        
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
    

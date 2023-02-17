from flask import jsonify, request
from flask.views import MethodView
from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from src.api.matricula import schemas
from src.models.matriculas import MatriculaModel
from src.db import db
from marshmallow import ValidationError
from src.models.alunos import AlunoModel
from src.models.cursos import CursoModel
from datetime import datetime


class MatriculaView(MethodView):    
    schema = schemas.MatriculaSchema
    model = MatriculaModel
    
    def get(self):
        # breakpoint()
        matriculas = self.model.query.all()
        return jsonify(self.schema(many=True).dump(matriculas)), 200
    
    def post(self, curso_id, aluno_id):
        # breakpoint()
        aluno = AlunoModel.query.get(aluno_id)
        if not aluno:
            return jsonify("Aluno not found."), 404
        curso = CursoModel.query.get(curso_id)
        if not curso:
            return jsonify("Curso not found."), 404
        
        matricula = {
            "aluno": aluno.id,
            "curso": curso.id,
            "status": True,
            "ano": datetime.utcnow().strftime("%B")
        }
      
        matricula = self.model(**matricula)
        db.session.add(matricula)
        db.session.commit()
        
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
    
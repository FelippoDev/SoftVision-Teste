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
        matriculas = self.model.query.all()
        return jsonify(self.schema(many=True).dump(matriculas)), 200
    
    def post(self, curso_id, aluno_id):
        aluno = AlunoModel.query.get(aluno_id)
        if not aluno:
            return jsonify("Aluno not found."), 404
        curso = CursoModel.query.get(curso_id)
        if not curso:
            return jsonify("Curso not found."), 404
       
        cursos = aluno.cursos
        for c in cursos:
            if c.id == curso.id:
                return jsonify("Matricula already made."), 400
            
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
        matricula = self.model.query.get(id)
        if matricula is None:
            return jsonify({'error': 'Matricula Not Found.'}), 404
        
        if not matricula.status:
            if data['status']:
                matricula.data_cadastro = datetime.utcnow()
            
        matricula.status = data['status']
   
        db.session.add(matricula)
        db.session.commit()
        return jsonify(self.schema().dump(matricula)), 201
    
    
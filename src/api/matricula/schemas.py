from marshmallow import fields, Schema
from src.api.aluno.schemas import PlainAlunoSchema
from src.api.curso.schemas import PlainCursoSchema
from src.models.matriculas import MatriculaModel


class MatriculaSchema(Schema):
    class Meta:
        model = MatriculaModel
        include_relationships = True
        load_instance = True
    
    id = fields.Integer(dump_only=True)    
    aluno = fields.Integer(required=True)
    curso = fields.Integer(required=True)
    status = fields.Boolean(required=True)
    ano = fields.String()
    data_cadastro = fields.DateTime()
    

class CursoSchema(PlainCursoSchema):           
    alunos = fields.List(fields.Nested(PlainAlunoSchema()), dump_only=True)
    
    
class AlunoSchema(PlainAlunoSchema):
  cursos = fields.List(fields.Nested(CursoSchema()), dump_only=True)
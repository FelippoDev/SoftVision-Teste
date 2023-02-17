from marshmallow import fields, Schema
from src.api.aluno.schemas import PlainAlunoSchema
from src.api.curso.schemas import PlainCursoSchema


class CursoSchema(PlainCursoSchema):
    alunos = fields.List(fields.Nested(PlainAlunoSchema()), dump_only=True)
    
    
class AlunoSchema(PlainAlunoSchema):
  cursos = fields.List(fields.Nested(CursoSchema()), dump_only=True)
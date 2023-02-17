from marshmallow import fields, Schema
from src.models.alunos import AlunoModel

class PlainAlunoSchema(Schema):
    class Meta:
        model = AlunoModel
        include_relationships = True
        load_instance = True

    id = fields.Integer(dump_only=True)
    nome = fields.String(required=True)
    cpf = fields.String(required=True)
    email = fields.Email(required=True)
    status = fields.Boolean(required=True)
    data_nascimento = fields.Date(required=True)
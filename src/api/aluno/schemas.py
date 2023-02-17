from marshmallow import fields, Schema
from src.models.alunos import AlunoModel


class AlunoSchema(Schema):
    class Meta:
        model = AlunoModel
        include_relationships = True
        load_instance = True

    id = fields.Integer()
    nome = fields.String(required=True)
    cpf = fields.String(required=True)
    email = fields.Email(required=True)
    status = fields.Boolean(required=True)
    data_nascimento = fields.Date(required=True)


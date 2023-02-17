from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemySchema

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



# class AlunoUpdateSchema(Schema):
#     ...
    
    
# class CursoSchema(Schema):
#     nome = fields.String(required=True)
#     status = fields.Boolean(required=True)
#     slug = fields.String(required=True)
#     sequencia = fields.Integer(required=True)
#     precoVenda = fields.Decimal(required=True)
#     dataCadastro = fields.DateTime(required=True)
    


# class CursoUpdateSchema(Schema):
#     id = fields.Number(as_string=True)
#     nome = fields.String(required=True)
#     status = fields.Boolean(required=True)
#     slug = fields.String(required=True)
#     sequencia = fields.Integer(required=True)
#     precoVenda = fields.Decimal(required=True)
#     dataCadastro = fields.DateTime(required=True)
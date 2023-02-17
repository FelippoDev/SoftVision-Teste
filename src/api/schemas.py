from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemySchema

from src.models.alunos import AlunoModel
from src.models.cursos import CursoModel


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
    
    
class CursoSchema(Schema):
    class Meta:
        model = CursoModel
        include_relationships = True
        load_instance = True
        
        
    id = fields.Integer()    
    nome = fields.String(required=True)
    status = fields.Boolean(required=True)
    slug = fields.String()
    sequencia = fields.Integer(required=True)
    preco_venda = fields.Decimal()
    data_cadastro = fields.DateTime()
    


# class CursoUpdateSchema(Schema):
#     id = fields.Number(as_string=True)
#     nome = fields.String(required=True)
#     status = fields.Boolean(required=True)
#     slug = fields.String(required=True)
#     sequencia = fields.Integer(required=True)
#     precoVenda = fields.Decimal(required=True)
#     dataCadastro = fields.DateTime(required=True)
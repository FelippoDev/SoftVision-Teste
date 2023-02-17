from flask import Blueprint
from . import views

api = Blueprint('api', __name__, url_prefix="/api")


api.add_url_rule('/aluno/list', view_func=views.AlunoListView.as_view('list-aluno'))
api.add_url_rule('/create/aluno', view_func=views.AlunoView.as_view('create-aluno'))
api.add_url_rule('/aluno/<int:id>', view_func=views.AlunoView.as_view('aluno'))


api.add_url_rule('/curso/list', view_func=views.CursoListView.as_view('list-curso'))
api.add_url_rule('/create/curso', view_func=views.CursoView.as_view('create-curso'))
api.add_url_rule('/curso/<int:id>', view_func=views.CursoView.as_view('curso'))



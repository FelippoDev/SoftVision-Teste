from api.urls import api
from api.aluno import views

api.add_url_rule('/aluno/list', view_func=views.AlunoListView.as_view('list-aluno'))
api.add_url_rule('/create/aluno', view_func=views.AlunoView.as_view('create-aluno'))
api.add_url_rule('/aluno/<int:id>', view_func=views.AlunoView.as_view('aluno'))
from django.urls import path
from .views import index, base, emprestimo, inicial, itensCadastroDevolutivos, itensCadastroNaoDevolutivos, itensVisualizacao, usuariosCadastro, usuariosVisualizacao

urlpatterns = [
    path('base/', base, name='base'),
    path('emprestimo/', emprestimo, name='emprestimo'),
    path('', index, name='index'),
    path('inicial/', inicial, name='inicial'),
    path('itensCadastroDevolutivos/', itensCadastroDevolutivos, name='itensCadastroDevolutivos'),
    path('itensCadastroNaoDevolutivos/', itensCadastroNaoDevolutivos, name='itensCadastroNaoDevolutivos'),
    path('itensVisualizacao/', itensVisualizacao, name='itensVisualizacao'),
    path('usuarioCadastro/', usuariosCadastro, name='usuarioCadastro'),
    path('usuarioVisualizacao/', usuariosVisualizacao, name='usuarioVisualizacao'),
]
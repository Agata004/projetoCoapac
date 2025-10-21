from django.urls import path
from .views import index, base, emprestimos, inicial, itensCadastroDevolutivos, itensCadastroNaoDevolutivos, itensVisualizacao, usuariosCadastro, usuariosVisualizacao

urlpatterns = [
    path('base/', base, name='base'),
    path('emprestimos/', emprestimos, name='emprestimos'),
    path('', index, name='index'),
    path('inicial/', inicial, name='inicial'),
    path('itensCadastroDevolutivos/', itensCadastroDevolutivos, name='itensCadastroDevolutivos'),
    path('itensCadastroNaoDevolutivos/', itensCadastroNaoDevolutivos, name='itensCadastroNaoDevolutivos'),
    path('itensVisualizacao/', itensVisualizacao, name='itensVisualizacao'),
    path('usuarioCadastro/', usuariosCadastro, name='usuarioCadastro'),
    path('usuarioVisualizacao/', usuariosVisualizacao, name='usuarioVisualizacao'),
]
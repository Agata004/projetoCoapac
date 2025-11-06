from django.urls import path
from .views import index, base, inicial, itensCadastro, itensVisualizacao, tipoItensVisualizacao, tipoItensCadastro
from .views import usuariosCadastro, usuariosVisualizacao, usuarios_editar, usuarios_delete  
from .views import emprestimo

urlpatterns = [
    path('base/', base, name='base'),
    path('emprestimo/', emprestimo, name='emprestimo'),
    path('', index, name='index'),
    path('inicial/', inicial, name='inicial'),
    path('itensCadastro/', itensCadastro, name='itensCadastro'),
    path('tipoItensVisualizacao/', tipoItensVisualizacao, name='tipoItensVisualizacao'),
    path('tipoItensCadastro/', tipoItensCadastro, name='tipoItensCadastro'),
    path('itensVisualizacao/', itensVisualizacao, name='itensVisualizacao'),
    path('usuariosCadastro/', usuariosCadastro, name='usuariosCadastro'),
    path('usuariosVisualizacao/', usuariosVisualizacao, name='usuariosVisualizacao'),
    path('usuariosCadastro/<int:credencial>/', usuarios_editar, name='usuariosEditar'),
    path('usuariosVisualizacao/<int:credencial>/', usuarios_delete, name='usuariosDelete'),
]
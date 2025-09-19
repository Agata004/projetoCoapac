"""
URL configuration for projetoCoapac project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import index, materiais, emprestimos, itensEmpres, estoque, dias, salas, reservas, confReser, base, usuario, usuarios, teste, inicio, impressões, controle, icones

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('materiais/', materiais, name='materiais'),
    path('itensEmpres/', itensEmpres, name='itensEmpres'),
    path('emprestimos/', emprestimos, name='emprestimos'),
    path('estoque/', estoque, name='estoque'),
    path('inicio/', inicio, name='inicio'),
    path('dias/', dias, name='dias'),
    path('salas/', salas, name='salas'),
    path('reservas/', reservas, name='reservas'),
    path('base/', base, name='base'),
    path('confReser/', confReser, name='confReser'),
    path('usuario/', usuario, name='usuario'),
    path('usuarios/', usuarios, name='usuarios'),
    path('teste/', teste, name='teste'),
    path('impressões/', impressões, name='impressões'),
    path('controle/', controle, name='controle'),
     path('icones/', icones, name='icones'),
]

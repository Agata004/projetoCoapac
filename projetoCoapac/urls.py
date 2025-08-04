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
<<<<<<< HEAD
from core.views import index, materiais, emprestimos, itens, estoque, dias, salas, reservas, bases
=======
from core.views import index, materiais, emprestimos, itens, estoque, dias, salas, reservas, teste, confReser
>>>>>>> cf9bd113ee024989a9631340d1d18d47bbf0a54f

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('materiais/', materiais, name='materiais'),
    path('itens/', itens, name='itens'),
    path('emprestimos/', emprestimos, name='emprestimos'),
    path('estoque/', estoque, name='estoque'),
    path('dias/', dias, name='dias'),
    path('salas/', salas, name='salas'),
    path('reservas/', reservas, name='reservas'),
<<<<<<< HEAD
    path('bases/', bases, name='bases'),
=======
    path('teste/', teste, name='teste'),
    path('confReser/', confReser, name='confReser'),
>>>>>>> cf9bd113ee024989a9631340d1d18d47bbf0a54f
]

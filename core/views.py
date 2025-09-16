from django.shortcuts import render
from .models import Usuario

# Ordenar alfabeticamente para encontrar mais fácil
def AeP(request):
    return render(request, 'AeP.html')
def base(request):
    return render (request, 'base.html')
def confReser(request):
    return render (request, 'confReser.html')
def dias(request):
    return render (request, 'dias.html')
def emprestimos(request):
    return render (request, 'emprestimos.html')
def estoque(request):
    return render (request, 'estoque.html')
def index(request):
    return render (request, 'index.html')
def inicio(request):
    return render (request, 'inicio.html')
def itensEmpres(request):
    return render (request, 'itensEmpres.html')
def materiais(request):
    return render (request, 'materiais.html')
def reservas(request):
    return render (request, 'reservas.html')
def salas(request):
    return render (request, 'salas.html')
def usuario(request):
    novo_usuario = Usuario()
    novo_usuario.credencial = request.POST.get('credencial')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.save()
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render (request, 'usuario.html', usuarios)
def usuarios(request):
    return render (request, 'usuarios.html')
def teste(request):
    return render (request, 'testedelinks.html')
def impressões(request):
    return render (request, 'impressões.html')
def controle(request):
    return render (request, 'controle.html')




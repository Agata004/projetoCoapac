from django.shortcuts import render

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
def usuarios(request):
    return render (request, 'usuarios.html')

def teste(request):
    return render (request, 'testedelinks.html')
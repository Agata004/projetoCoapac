from django.shortcuts import render

def index(request):
    return render (request, 'index.html')
def materiais(request):
    return render (request, 'materiais.html')
def itens(request):
    return render (request, 'itens.html')
def emprestimos(request):
    return render (request, 'emprestimos.html')
def estoque(request):
    return render (request, 'estoque.html')
def dias(request):
    return render (request, 'dias.html')
def salas(request):
    return render (request, 'salas.html')
def reservas(request):
    return render (request, 'reservas.html')
def bases(request):
    return render (request, 'bases.html')
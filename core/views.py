from django.shortcuts import render

def index(request):
    return render (request, 'index.html')
def materiais(request):
    return render (request, 'materiais.html')
<<<<<<< HEAD
def itens(request):
    return render (request, 'itens.html')
def emprestimos(request):
    return render (request, 'emprestimos.html')
def estoque(request):
    return render (request, 'estoque.html')
=======
>>>>>>> 6e76506336cd7eb7aa38ea3995c45e8d9c926b0d

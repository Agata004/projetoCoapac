from django.shortcuts import render

# Ordenar alfabeticamente para encontrar mais fácil
def index(request):
    return render(request, 'index.html')
def base(request):
    return render(request, 'base.html')
def emprestimos(request):
    return render(request, 'emprestimos.html')
def inicial(request):
    return render(request, 'inicial.html')
def itensCadastroDevolutivos(request):
    return render(request, 'itensCadastroDevolutivos.html')
def itensCadastroNaoDevolutivos(request):
    return render(request, 'itensCadastroNaoDevolutivos.html')
def itensVisualizacao(request):
    return render(request, 'itensVisualizacao.html')
def usuariosCadastro(request):
    return render(request, 'usuarioCadastro.html')
def usuariosVisualizacao(request):
    return render(request, 'usuarioVisualizacao.html')
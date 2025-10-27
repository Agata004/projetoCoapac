from django.shortcuts import render, redirect
from .models import Usuario

# Ordenar alfabeticamente para encontrar mais fácil
def index(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        senha = request.POST.get('senha')
        
        # Verificar se os campos não estão vazios
        if not login or not senha:
            return render(request, 'index.html', {'toast': 'Login e senha não podem estar vazios.'})
            
        try:
            # Tenta encontrar um usuário com a credencial e senha fornecidas
            usuario = Usuario.objects.get(credencial=login, senha=senha)
            
            # Se encontrou o usuário, verifica se é admin (credencial 1)
            if usuario.credencial == '1':
                return redirect('usuarioVisualizacao')
            else:
                return redirect('inicial')
                
        except Usuario.DoesNotExist:
            # Se não encontrou o usuário, retorna para o index com mensagem de erro
            return render(request, 'index.html', {'toast': 'Credencial ou senha inválidos.'})
    return render(request, 'index.html')
def base(request):
    return render(request, 'base.html')
def emprestimo(request):
    return render(request, 'emprestimo.html')
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
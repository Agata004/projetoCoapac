from django.shortcuts import render, redirect
from .models import ComunidadeEscolar, Usuarios, TipoProduto, Produtos, Emprestimo
from .forms import ComunidadeEscolarForm, UsuariosForm, TipoProdutoForm, ProdutosForm, EmprestimoForm


# Ordenar alfabeticamente para encontrar mais fácil
def index(request):
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

# Usuários
def usuariosVisualizacao(request):
    usuarios = Usuarios.objects.all()
    contexto = {
        'usuarios': usuarios
    }
    return render(request, 'usuariosVisualizacao.html', contexto)

def usuariosCadastro(request):
    form = UsuariosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('usuariosVisualizacao')
    
    contexto = {
        'form': form
    }
    return render(request, 'usuariosCadastro.html', contexto)

def usuarios_editar(request, credencial):
    usuarios = Usuarios.objects.get(credencial=credencial)
    form = UsuariosForm(request.POST or None, instance=usuarios)
    if form.is_valid():
        form.save()
        return redirect('usuariosVisualizacao')
    
    contexto = {
        'form': form
    }
    return render(request, 'usuariosCadastro.html', contexto)
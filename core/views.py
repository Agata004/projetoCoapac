from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ComunidadeEscolar, Usuarios, TipoProduto, Emprestimo
from .forms import UsuariosForm, TipoProdutoForm, EmprestimoForm

# Ordenar alfabeticamente para encontrar mais fácil
def index(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        senha = request.POST.get('senha')   
        try:
            # Tenta encontrar um usuário pela credencial
            usuario = Usuarios.objects.get(credencial=login)
            # Verifica se a senha está correta
            if usuario.check_password(senha):
                # Se a senha está correta, verifica se é admin (credencial 1)
                if int(login) == 412365:
                    return redirect('usuariosVisualizacao')
                else:
                    return redirect('inicial')
            else:
                # Senha incorreta
                return render(request, 'index.html', {'toast': 'Credencial ou senha inválidos.'})
                
        except Usuarios.DoesNotExist:
            # Se não encontrou o usuário, retorna para o index com mensagem de erro
            return render(request, 'index.html', {'toast': 'Credencial ou senha inválidos.'})
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

# Empréstimo
def emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            try:
                # Trata produto
                #produto_nome = request.POST.get('produtos')
                #produto = Produtos.objects.get(nome=produto_nome)

                # Trata usuário responsável
                usuario_nome = request.POST.get('usuarios')
                usuario = Usuarios.objects.get(nome=usuario_nome)

                # Trata comunidade escolar: cria se não existir
                comunidade_nome = request.POST.get('comunidadeEscolar')
                comunidade_matricula = request.POST.get('matricula')
                comunidade_vinculo = request.POST.get('vinculo')
                comunidade_turma = request.POST.get('turma_disciplina')

                comunidade, created = ComunidadeEscolar.objects.get_or_create(
                    matricula=comunidade_matricula,
                    defaults={
                        'nome': comunidade_nome,
                        'vinculo': comunidade_vinculo,
                        'turmaouDisciplina': comunidade_turma
                    }
                )
                # Se já existia, atualiza os campos caso queira manter consistência
                if not created:
                    comunidade.nome = comunidade_nome
                    comunidade.vinculo = comunidade_vinculo
                    comunidade.turmaouDisciplina = comunidade_turma
                    comunidade.save()

                # Cria o empréstimo
                emprestimo = form.save(commit=False)
                #emprestimo.produtos = produto
                emprestimo.usuarios = usuario
                emprestimo.comunidadeEscolar = comunidade
                emprestimo.save()

                messages.success(request, 'Empréstimo cadastrado com sucesso!')
                return redirect('inicial')

            #except Produtos.DoesNotExist:
            #    messages.error(request, f'O produto "{produto_nome}" não foi encontrado. Por favor, verifique o nome do produto.')
            except Usuarios.DoesNotExist:
                messages.error(request, f'O usuário "{usuario_nome}" não foi encontrado. Por favor, verifique o nome do usuário.')
            except Exception as e:
                messages.error(request, f'Ocorreu um erro inesperado: {str(e)}')
        else:
            messages.error(request, 'Erro ao validar o formulário. Por favor, verifique os dados inseridos.')
    else:
        form = EmprestimoForm()

    return render(request, 'emprestimo.html', {'form': form, 'editar': False})

def inicial(request):
    emprestimos = Emprestimo.objects.select_related('produtos', 'usuarios', 'comunidadeEscolar')
    contexto = {
        'emprestimos': emprestimos
    }
    return render(request, 'inicial.html', contexto)

# Itens/Produtos
def itensCadastro(request):
    return render(request, 'itensCadastro.html')
def itensVisualizacao(request):
    return render(request, 'itensVisualizacao.html')

# Tipo de Itens/Produtos
def tipoItensVisualizacao(request):
    tipos = TipoProduto.objects.all()
    contexto = {
        'tipos': tipos
    }
    return render(request, 'tipoItensVisualizacao.html', contexto)

def tipoItensCadastro(request):
    form = TipoProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Tipo de produto cadastrado com sucesso.')
        return redirect('tipoItensVisualizacao')
    
    contexto = {
        'form': form
    }
    return render(request, 'tipoItensCadastro.html', contexto)

def tipoItensEditar(request, codigo):
    tipos = get_object_or_404(TipoProduto, codigo=codigo)
    form = TipoProdutoForm(request.POST or None, instance=tipos)

    form.fields['codigo'].widget.attrs['readonly'] = True # Impede edição do campo código

    if request.method == 'POST':
        if form.is_valid():
            tipos.nome = form.cleaned_data['nome']
            tipos.save()
            messages.success(request, 'Tipo de produto atualizado com sucesso.')
            return redirect('tipoItensVisualizacao')
    else:
        # Preenche manualmente os valores no contexto, sem usar o ModelForm instance
        contexto = {
            'form': form,
            'codigo': tipos.codigo,
            'nome': tipos.nome
        }
        return render(request, 'tipoItensCadastro.html', contexto)
    
    contexto = {
        'form': form
    }
    return render(request, 'tipoItensCadastro.html', contexto)

def tipoItensDelete(request, codigo):
    tipos = get_object_or_404(TipoProduto, codigo=codigo)
    if request.method == 'POST':
        tipos.delete()
        messages.success(request, 'Tipo de produto excluído com sucesso.')
    return redirect('tipoItensVisualizacao')

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
        messages.success(request, 'Usuário cadastrado com sucesso.')
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
        messages.success(request, 'Usuário atualizado com sucesso.')
        return redirect('usuariosVisualizacao')
    
    contexto = {
        'form': form
    }
    return render(request, 'usuariosCadastro.html', contexto)

def usuarios_delete(request, credencial):
    usuarios = get_object_or_404(Usuarios, credencial=credencial)
    if request.method == 'POST':
        usuarios.delete()
        messages.success(request, 'Usuário excluído com sucesso.')
        return redirect('usuariosVisualizacao')
    contexto = {
        'usuarios': usuarios
    }
    return render(request, 'usuarios_confirm_delete.html', contexto)
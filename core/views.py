from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError, transaction
from django.contrib import messages
from .models import ComunidadeEscolar, Usuarios, TipoProduto, Produtos, Emprestimo
from .forms import UsuariosForm, TipoProdutoForm, EmprestimoForm, ProdutosForm

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
    if not request.user.is_authenticated:
        messages.error(request, "Você precisa estar logado para registrar empréstimos.")
        return redirect('login')  # ajuste para sua rota de login

    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            # campos vindos do formulário HTML (requerente)
            requerente_nome = request.POST.get('requerente', '').strip()
            matricula = request.POST.get('matricula', '').strip()
            vinculo = request.POST.get('vinculo', '').strip()
            turma = request.POST.get('turma_disciplina', '').strip()

            # pega o produto selecionado
            produto = form.cleaned_data.get('produtos')
            if not produto:
                form.add_error('produtos', 'Selecione um produto válido.')
                # volta ao template com erros
                return render(request, 'emprestimo.html', {'form': form, 'usuario_logado': request.user})
            
            if Emprestimo.objects.filter(produtos=produto, entregue=False).exists():
                form.add_error('produtos', 'Este produto já está emprestado e não foi devolvido.')
                # volta ao template com erros
                return render(request, 'emprestimo.html', {'form': form, 'usuario_logado': request.user})

            # usa transação para evitar corrida que crie duplicatas da Comunidade
            try:
                with transaction.atomic():

                    # get_or_create por matrícula
                    if matricula:
                        comunidade, created = ComunidadeEscolar.objects.get_or_create(
                            matricula=matricula,
                            defaults={
                                'nome': requerente_nome,
                                'vinculo': vinculo,
                                'turmaouDisciplina': turma
                            }
                        )
                        # se já existia, atualiza campos se necessário
                        if not created:
                            updated = False
                            if requerente_nome and comunidade.nome != requerente_nome:
                                comunidade.nome = requerente_nome
                                updated = True
                            if vinculo and comunidade.vinculo != vinculo:
                                comunidade.vinculo = vinculo
                                updated = True
                            if turma and comunidade.turmaouDisciplina != turma:
                                comunidade.turmaouDisciplina = turma
                                updated = True
                            if updated:
                                comunidade.save()
                    else:
                        form.add_error('matricula', 'Matrícula é obrigatória.')
                        return render(request, 'emprestimo.html', {'form': form, 'usuario_logado': request.user})

                    # cria o empréstimo sem commitar ainda
                    emprestimo = form.save(commit=False)
                    emprestimo.produtos = produto
                    emprestimo.usuarios = request.user
                    emprestimo.comunidadeEscolar = comunidade
                    emprestimo.save()

                messages.success(request, 'Empréstimo cadastrado com sucesso!')
                return redirect('inicial')
            except Exception as e:
                # captura erros inesperados
                form.add_error(None, f'Erro ao salvar empréstimo: {e}')
    else:
        form = EmprestimoForm()

    contexto = {
        'form': form,
        'usuario_logado': request.user
    }
    return render(request, 'emprestimo.html', contexto)


def inicial(request):
    emprestimos = Emprestimo.objects.select_related('produtos', 'usuarios', 'comunidadeEscolar')
    contexto = {
        'emprestimos': emprestimos
    }
    return render(request, 'inicial.html', contexto)

# Itens/Produtos
def itensVisualizacao(request):
    devolutivos = Produtos.objects.filter(devo_ou_nao=True)
    nao_devolutivos = Produtos.objects.filter(devo_ou_nao=False)

    contexto = {
        'devolutivos': devolutivos,
        'nao_devolutivos': nao_devolutivos
    }
    return render(request, 'itensVisualizacao.html', contexto)

def itensCadastro(request):
    form = ProdutosForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Item cadastrado com sucesso.')
            return redirect('itensVisualizacao')
    
    contexto = {
        'form': form
    }
    return render(request, 'itensCadastro.html', contexto)

# Tipo de Itens/Produtos
def tipoItensVisualizacao(request):
    tipos = TipoProduto.objects.all()
    contexto = {
        'tipos': tipos
    }
    return render(request, 'tipoItensVisualizacao.html', contexto)

def tipoItensCadastro(request):
    form = TipoProdutoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Tipo de produto cadastrado com sucesso.')
            except IntegrityError:
                # Mensagem quando o código já existe
                messages.error(request, 'O código informado já existe. Por favor, escolha outro.')
            return redirect('tipoItensVisualizacao')
        else:
            messages.error(request, 'Erro ao cadastrar tipo de produto. Verifique os dados inseridos.')

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
        messages.success(request, 'Tipo de produto excluído com sucesso.', extra_tags='exclusao')
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
    usuarios = get_object_or_404(Usuarios, credencial=credencial)
    form = UsuariosForm(request.POST or None, instance=usuarios)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário atualizado com sucesso.')
            return redirect('usuariosVisualizacao')
    else:
        # Preenche manualmente os valores no contexto (sem alterar estrutura principal)
        contexto = {
            'form': form,
            'editar': True
        }
        return render(request, 'usuariosCadastro.html', contexto)
    
    contexto = {
        'form': form,
        'editar': True
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
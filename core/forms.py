from django import forms
from .models import ComunidadeEscolar, Usuarios, TipoProduto, Produtos, Emprestimo

class ComunidadeEscolarForm(forms.ModelForm):
    class Meta:
        model = ComunidadeEscolar
        fields = ['matricula', 'nome', 'vinculo', 'turmaouDisciplina']

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['credencial', 'nome', 'senha']

class TipoProdutoForm(forms.ModelForm):
    class Meta:
        model = TipoProduto
        fields = ['nome']

class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome', 'marca', 'tipoProduto']

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['dataSaida', 'dataDevolucao', 'produtos', 'comunidadeEscolar', 'usuarios']
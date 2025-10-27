from django import forms
from .models import ComunidadeEscolar, Usuarios, TipoProduto, Produtos, Emprestimo

class ComunidadeEscolarForm(forms.ModelForm):
    class Meta:
        model = ComunidadeEscolar
        fields = ['matricula', 'nome', 'vinculo', 'turmaouDisciplina']

class UsuariosForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Usuarios
        fields = ['credencial', 'nome', 'senha']
        
    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data['senha'])
        if commit:
            usuario.save()
        return usuario

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
from django import forms
from .models import Usuarios, TipoProduto, Produtos, Emprestimo

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
        fields = ['nome', 'codigo']

class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome', 'marca', 'tipoProduto', 'devo_ou_nao']
        widgets = {
            'tipoProduto': forms.Select(attrs={'class': 'form-select'}),
            'devo_ou_nao': forms.RadioSelect(choices=[(True, 'Devolutivo'), (False, 'Não Devolutivo')])
        }

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['dataSaida', 'dataDevolucao', 'comunidadeEscolar', 'usuarios']
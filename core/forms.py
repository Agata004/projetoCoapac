from django import forms
from .models import Usuarios, TipoProduto, Produtos, Emprestimo
from django.contrib.auth.forms import UserCreationForm

class UsuariosForm(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = ['credencial', 'username', 'nome', 'password1', 'password2']


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
        fields = ['dataSaida', 'dataDevolucao', 'entregue', 'produtos']
        widgets = {
            'produtos': forms.Select(attrs={'class': 'form-select'}),
            'dataSaida': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'dataDevolucao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dataDevolucao'].required = False
    
    def clean(self):
        cleaned_data = super().clean()
        data_saida = cleaned_data.get('dataSaida')
        data_devolucao = cleaned_data.get('dataDevolucao')

        if data_saida and data_devolucao:
            if data_devolucao < data_saida:
                raise forms.ValidationError(
                    "A data de entrega não pode ser anterior à data de saída."
                )
        return cleaned_data
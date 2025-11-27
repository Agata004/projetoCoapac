from django import forms
from .models import Usuarios, TipoProduto, Produtos, Emprestimo
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UsuariosForm(UserCreationForm):
    class Meta:
        model = Usuarios
        fields = ['credencial', 'username', 'nome']

class UsuariosEditForm(UserChangeForm):
    password = None  # esconde o campo password padrão do UserChangeForm
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Confirmação de senha', widget=forms.PasswordInput, required=False)

    class Meta:
        model = Usuarios
        fields = ['credencial', 'username', 'nome']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Torna credencial somente leitura
        self.fields['credencial'].disabled = True

    def clean_credencial(self):
        # Garante que a credencial original não seja alterada
        return self.instance.credencial

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('password1')
        senha2 = cleaned_data.get('password2')
        if senha or senha2:
            if senha != senha2:
                self.add_error('password2', "As senhas não coincidem.")
        return cleaned_data


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
from django import forms
from django.core.exceptions import ValidationError
from .models import Loja, formatar_endereco

class LojaForm(forms.ModelForm):
    class Meta:
        model = Loja
        fields = ['nome', 'endereco', 'bairro', 'cep', 'telefone', 'imagem']

    def clean_endereco(self):
        endereco = self.cleaned_data.get('endereco')
        if not endereco or len(endereco) < 10:
            raise ValidationError('O endereço deve ter pelo menos 10 caracteres.')
        return formatar_endereco(endereco)  # Formatar o endereço aqui também

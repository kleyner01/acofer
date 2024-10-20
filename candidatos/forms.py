from django import forms
from . import models
import re


class CandidatoForm(forms.ModelForm):
    possui_habilitacao = forms.ChoiceField(choices=[(True, 'Sim'), (False, 'Não')], widget=forms.RadioSelect)
    tipo_habilitacao = forms.MultipleChoiceField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], widget=forms.CheckboxSelectMultiple, required=False)
    possui_carteira_profissional = forms.ChoiceField(choices=[(True, 'Sim'), (False, 'Não')], widget=forms.RadioSelect)
    serie_carteira_profissional = forms.ChoiceField(choices=[('A', 'Série A'), ('B', 'Série B'), ('C', 'Série C'), ('D', 'Série D'),], widget=forms.Select, required=False)

    class Meta:
        model = models.Candidato
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome completo', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu email', 'required': True}),
            'prefixo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: +55'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone'}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Celular'}),
            'curriculo': forms.FileInput(attrs={'class': 'form-control'}),
            'foto_perfil': forms.FileInput(attrs={'class': 'form-control'}),
            'data_nasc': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado_civil': forms.Select(attrs={'class': 'form-select'}),
            'rg': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RG'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite somente números do seu CPF', 'type': 'tel', 'pattern': '[0-9]*', 'inputmode': 'numeric'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'nome_pai': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pai'}),
            'nome_mae': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mãe'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Endereço completo'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CEP'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'possui_habilitacao': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tipo_habilitacao': forms.CheckboxSelectMultiple(attrs={'class': 'form-select'}),
            'possui_carteira_profissional': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'serie_carteira_profissional': forms.Select(attrs={'class': 'form-select'}),
            'formacao': forms.Select(attrs={'class': 'form-select'}),
            'curso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do curso'}),
            'ano_conclusao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ano de conclusão'}),
            'empresa_atual': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da empresa atual'}),
            'segmento_atual': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segmento'}),
            'cargo_atual': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cargo atual'}),
            'data_inicio_atual': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_saida_atual': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'atribuicoes_atual': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Atribuições na empresa atual'}),
            'empresa_anterior_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Empresa anterior 1'}),
            'segmento_anterior_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segmento'}),
            'cargo_anterior_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cargo anterior 1'}),
            'data_inicio_anterior_1': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_saida_anterior_1': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'atribuicoes_anterior_1': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Atribuições na empresa anterior 1'}),
            'empresa_anterior_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Empresa anterior 2'}),
            'segmento_anterior_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Segmento'}),
            'cargo_anterior_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cargo anterior 2'}),
            'data_inicio_anterior_2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_saida_anterior_2': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'atribuicoes_anterior_2': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Atribuições na empresa anterior 2'}),
            'cargo_pretendido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cargo pretendido'}),
            'faixa_salarial_desejada': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Faixa salarial'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva sua mensagem', 'rows': 3}),
        }

        labels = {
            'nome': 'Nome',
            'email': 'E-mail',
            'prefixo': 'Prefixo',
            'telefone': 'Telefone',
            'celular': 'Celular',
            'curriculo': 'Currículo',
            'foto_perfil': 'Foto de Perfil',
            'mensagem': 'Mensagem',
            'endereco': 'Endereço Completo',
            'numero': 'Número',
            'bairro': 'Bairro',
            'cep': 'CEP',
            'cidade': 'Cidade',
            'estado': 'Estado',
            'data_nasc': 'Data de Nascimento',
            'estado_civil': 'Estado Civil',
            'rg': 'RG',
            'cpf': 'CPF',
            'sexo': 'Sexo',
            'nome_pai': 'Nome do Pai',
            'nome_mae': 'Nome da Mãe',
            'possui_habilitacao': 'Possui Habilitação?',
            'tipo_habilitacao': 'Tipo de Habilitação',
            'possui_carteira_profissional': 'Possui Carteira Profissional?',
            'serie_carteira_profissional': 'Série da Carteira Profissional',
            'formacao': 'Formação Acadêmica',
            'curso': 'Curso',
            'ano_conclusao': 'Ano de Conclusão',
            'empresa_atual': 'Empresa Atual',
            'segmento_atual': 'Segmento Atual',
            'cargo_atual': 'Cargo Atual',
            'data_inicio_atual': 'Data de Início na Empresa Atual',
            'data_saida_atual': 'Data de Saída da Empresa Atual',
            'atribuicoes_atual': 'Atribuições na Empresa Atual',
            'empresa_anterior_1': 'Empresa Anterior 1',
            'segmento_anterior_1': 'Segmento Anterior 1',
            'cargo_anterior_1': 'Cargo Anterior 1',
            'data_inicio_anterior_1': 'Data de Início na Empresa Anterior 1',
            'data_saida_anterior_1': 'Data de Saída da Empresa Anterior 1',
            'atribuicoes_anterior_1': 'Atribuições na Empresa Anterior 1',
            'empresa_anterior_2': 'Empresa Anterior 2',
            'segmento_anterior_2': 'Segmento Anterior 2',
            'cargo_anterior_2': 'Cargo Anterior 2',
            'data_inicio_anterior_2': 'Data de Início na Empresa Anterior 2',
            'data_saida_anterior_2': 'Data de Saída da Empresa Anterior 2',
            'atribuicoes_anterior_2': 'Atribuições na Empresa Anterior 2',
            'cargo_pretendido': 'Cargo Pretendido',
            'faixa_salarial_desejada': 'Faixa Salarial Desejada',
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if cpf:
            cpf = re.sub(r'\D', '', cpf)
            if len(cpf) != 11 or not self.is_valid_cpf(cpf):
                raise forms.ValidationError("Certifique-se de que o CPF é válido e tem exatamente 11 dígitos.")
        return cpf

    def is_valid_cpf(self, cpf):
        if len(cpf) != 11 or not cpf.isdigit():
            return False

        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        primeiro_digito = 11 - (soma % 11)
        primeiro_digito = 0 if primeiro_digito >= 10 else primeiro_digito

        if int(cpf[9]) != primeiro_digito:
            return False

        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        segundo_digito = 11 - (soma % 11)
        segundo_digito = 0 if segundo_digito >= 10 else segundo_digito

        if int(cpf[10]) != segundo_digito:
            return False

        return True

    def clean_possui_habilitacao(self):
        possui_habilitacao = self.cleaned_data.get('possui_habilitacao')
        if possui_habilitacao is None:
            raise forms.ValidationError("Selecione se possui habilitação.")
        return possui_habilitacao

    def clean_tipo_habilitacao(self):
        tipo_habilitacao = self.cleaned_data.get('tipo_habilitacao')
        possui_habilitacao = self.cleaned_data.get('possui_habilitacao')

        if possui_habilitacao == 'True' and not tipo_habilitacao:
            raise forms.ValidationError('Por favor, selecione pelo menos um tipo de habilitação.')

        return tipo_habilitacao

    def clean_possui_carteira_profissional(self):
        possui_carteira_profissional = self.cleaned_data.get('possui_carteira_profissional')
        if possui_carteira_profissional is None:
            raise forms.ValidationError("Selecione se possui carteira profissional.")
        return possui_carteira_profissional

    def clean_serie_carteira_profissional(self):
        serie_carteira_profissional = self.cleaned_data.get('serie_carteira_profissional')
        possui_carteira_profissional = self.cleaned_data.get('possui_carteira_profissional')

        if possui_carteira_profissional == 'True' and not serie_carteira_profissional:
            raise forms.ValidationError("Por favor, escolha uma série válida da carteira profissional.")

        return serie_carteira_profissional

    def clean(self):
        cleaned_data = super().clean()

        possui_habilitacao = cleaned_data.get('possui_habilitacao')
        possui_carteira_profissional = cleaned_data.get('possui_carteira_profissional')

        if possui_habilitacao == 'False':
            cleaned_data['tipo_habilitacao'] = None

        if possui_carteira_profissional == 'False':
            cleaned_data['serie_carteira_profissional'] = None

        return cleaned_data

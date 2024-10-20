from django.core.validators import RegexValidator
from django.db import models
from multiselectfield import MultiSelectField


cep_validator = RegexValidator(r'^\d{5}-?\d{3}$', 'Formato de CEP inválido. Use 12345-678 ou 12345678.')
cpf_validator = RegexValidator(r'^\d{11}$', 'O CPF deve conter 11 dígitos, apenas números.')
letras_apenas = RegexValidator(r'^[a-zA-ZÀ-ÿ\s]+$', 'Somente letras são permitidas.')
numeros_apenas = RegexValidator(r'^\d+$', 'Somente números são permitidos.')


class Candidato(models.Model):
    TIPO_HABILITACAO_CHOICES = (
        ('A', 'Tipo A'),
        ('B', 'Tipo B'),
        ('C', 'Tipo C'),
        ('D', 'Tipo D'),
    )

    SERIE_CARTEIRA_PROFISSIONAL = (
        ('A', 'Série A'),
        ('B', 'Série B'),
        ('C', 'Série C'),
        ('D', 'Série D'),
    )
    ESTADOS_CHOICES = [
        ('', 'Selecione Estado'),
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]

    class Sexo(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMININO = 'F', 'Feminino'

    class EstadoCivil(models.TextChoices):
        CASADO = 'CASADO', 'Casado'
        SOLTEIRO = 'SOLTEIRO', 'Solteiro'
        DIVORCIADO = 'DIVORCIADO', 'Divorciado'

    class Formacao(models.TextChoices):
        NULL = '', 'Selecione Opções'
        FUNDAMENTAL = 'FL', 'Fundamental'
        ENSINO_MEDIO = 'EM', 'Ensino Médio'
        GRAU_1_COMPLETO = '1C', '1º Grau Completo'
        GRAU_1_INCOMPLETO = '1I', '1º Grau Incompleto'
        GRAU_2_COMPLETO = '2C', '2º Grau Completo'
        GRAU_2_INCOMPLETO = '2I', '2º Grau Incompleto'
        SUPERIOR_COMPLETO = 'SC', 'Superior Completo'
        SUPERIOR_INCOMPLETO = 'SI', 'Superior Incompleto'
        POS_GRADUACAO = 'PG', 'Pós-Graduação'
        MBA = 'MBA', 'MBA'
        MESTRADO = 'ME', 'Mestrado'
        DOUTORADO = 'DO', 'Doutorado'

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, validators=[letras_apenas])
    email = models.EmailField(unique=True)
    prefixo = models.CharField(max_length=2, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    curriculo = models.FileField(upload_to='curriculos/', blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    data_nasc = models.DateField()
    estado_civil = models.CharField(max_length=10, choices=EstadoCivil.choices, default=EstadoCivil.SOLTEIRO)
    rg = models.CharField(max_length=20, validators=[numeros_apenas], blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True, validators=[cpf_validator])
    sexo = models.CharField(max_length=1, choices=Sexo.choices, default=Sexo.MASCULINO)
    nome_pai = models.CharField(max_length=100, validators=[letras_apenas], blank=True, null=True)
    nome_mae = models.CharField(max_length=100, validators=[letras_apenas], blank=True, null=True)
    endereco = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=200, validators=[letras_apenas])
    cep = models.CharField(max_length=10, validators=[cep_validator])
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=2, choices=ESTADOS_CHOICES, default='')
    possui_habilitacao = models.BooleanField()
    tipo_habilitacao = MultiSelectField(choices=TIPO_HABILITACAO_CHOICES, blank=True, null=True)
    possui_carteira_profissional = models.BooleanField()
    serie_carteira_profissional = models.CharField(max_length=10, choices=SERIE_CARTEIRA_PROFISSIONAL, blank=True, null=True)
    formacao = models.CharField(max_length=50, choices=Formacao.choices, default=Formacao.NULL)
    curso = models.CharField(max_length=500, blank=True, null=True)
    ano_conclusao = models.IntegerField(blank=True, null=True)
    empresa_atual = models.CharField(max_length=200, blank=True, null=True)
    segmento_atual = models.CharField(max_length=100, blank=True, null=True)
    cargo_atual = models.CharField(max_length=50, blank=True, null=True)
    data_inicio_atual = models.DateField(blank=True, null=True)
    data_saida_atual = models.DateField(blank=True, null=True)
    atribuicoes_atual = models.TextField(max_length=200, blank=True, null=True)

    empresa_anterior_1 = models.CharField(max_length=200, blank=True, null=True)
    segmento_anterior_1 = models.CharField(max_length=100, blank=True, null=True)
    cargo_anterior_1 = models.CharField(max_length=50, blank=True, null=True)
    data_inicio_anterior_1 = models.DateField(blank=True, null=True)
    data_saida_anterior_1 = models.DateField(blank=True, null=True)
    atribuicoes_anterior_1 = models.TextField(max_length=200, blank=True, null=True)

    empresa_anterior_2 = models.CharField(max_length=200, blank=True, null=True)
    segmento_anterior_2 = models.CharField(max_length=100, blank=True, null=True)
    cargo_anterior_2 = models.CharField(max_length=50, blank=True, null=True)
    data_inicio_anterior_2 = models.DateField(blank=True, null=True)
    data_saida_anterior_2 = models.DateField(blank=True, null=True)
    atribuicoes_anterior_2 = models.TextField(max_length=200, blank=True, null=True)

    cargo_pretendido = models.CharField(max_length=100, validators=[letras_apenas])
    faixa_salarial_desejada = models.CharField(max_length=100)
    mensagem = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.nome

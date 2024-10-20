from django.db import models
from django.core.exceptions import ValidationError

def formatar_endereco(endereco):
    # Formatar o endereço, por exemplo, capitalizando as palavras
    return ' '.join(word.capitalize() for word in endereco.split())

class Loja(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cep = models.CharField(max_length=10)
    telefone = models.CharField(max_length=15)
    imagem = models.ImageField(upload_to='path/lojas/')

    def clean(self):
        # Validação personalizada
        if not self.endereco or len(self.endereco) < 10:
            raise ValidationError('O endereço deve ter pelo menos 10 caracteres.')

    def save(self, *args, **kwargs):
        # Formatação antes de salvar
        self.endereco = formatar_endereco(self.endereco)  
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

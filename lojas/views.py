from django.shortcuts import render
from .models import Loja

def listar_lojas(request):
    lojas = Loja.objects.all()
    return render(request, 'loja.html', {'lojas': lojas})

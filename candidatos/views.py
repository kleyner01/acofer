from django.shortcuts import render, redirect
from .forms import CandidatoForm
from django.contrib import messages

def CandidatoListView(request):
    if request.method == 'POST':
        form = CandidatoForm(request.POST, request.FILES)
        if form.is_valid():
            print("possui habilitacao:", form.cleaned_data['possui_habilitacao'])
            print("tipo habilitacao:", form.cleaned_data['tipo_habilitacao'])
            print("possui carteira profissional:", form.cleaned_data['possui_carteira_profissional'])
            print("serie carteira profissional:", form.cleaned_data['serie_carteira_profissional'])
            form.save()
            messages.success(request, 'Candidato cadastrado com sucesso!')
            return redirect('sucessos')
        else:
            print(form.errors)
            messages.error(request, 'Erro ao enviar o formulário. Por favor, verifique os campos.')
    else:
        form = CandidatoForm()

    return render(request, 'trabalhe_conoscos.html', {'form': form})

def SucessosView(request):
    return render(request, 'sucessos.html')
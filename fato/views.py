from django.shortcuts import render, redirect
from .models import Fato
from .forms import FatoForm, VitimaForm, AutorForm, TestemunhaForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listar_fato(request):
    fatos = Fato.objects.all()
    return render(request, 'listar-fatos.html', {'fatos': fatos})

def criar_fato(request):
    form = FatoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_fato')
    
    return render(request, 'fato-form.html', {'form': form})

def update_fato(request, id):
    fato = Fato.objects.get(id=id)
    form = FatoForm(request.POST or None, instance=fato)

    if form.is_valid():
        form.save()
        return redirect('listar_fato')

    return render(request, 'fato-form.html', {'form': form, 'fato':fato})

def deletar_fato(request, id):
    fato = Fato.objects.get(id=id)

    if request.method =='POST':
        fato.delete()
        return redirect('listar_fato')

    return render(request, 'confirmar_deletar_fato.html', {'fato': fato})


def criar_vitima(request):
    form = VitimaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('criar_fato')

    return render(request, 'vitima-form.html', {'form': form})

def criar_autor(request):
    form = AutorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('criar_fato')

    return render(request, 'autor-form.html', {'form': form})

def criar_testemunha(request):
    form = TestemunhaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('criar_fato')

    return render(request, 'testemunha-form.html', {'form': form})




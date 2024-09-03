from django.shortcuts import render, redirect
from .models import Estudante
from .forms import EstudanteForm


# Create your views here.


def index(request):
    if request.method =='POST':
        form = EstudanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrados')
   
    else:
        print("entrando")
        form = EstudanteForm()
    contexto = {'form': form}
       
    return render(request, 'index.html', contexto)




def pessoas(request):
    contexto = {'cadastrados': Estudante.objects.all()}
    return render(request, 'cadastrados.html', contexto)
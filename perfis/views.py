from django.shortcuts import render
#from django.http import HttpResponse
from perfis.models import Perfil

# Create your views here.

def index(request):
    return render(request , 'index.html', {'perfis': Perfil.objects.all()})

def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    return render(request , 'perfil.html' , {'perfil' : perfil})
    ## terceiro parâmetro para a função render, que nada mais é do que um dicionário que contém a chave "perfil", que guarda o objeto perfil 

def convidar(request, perfil_id):
    pass
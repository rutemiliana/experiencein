from django.shortcuts import render
#from django.http import HttpResponse
from perfis.models import Perfil

# Create your views here.

def index(request):
    return render(request , 'index.html')

def exibir(request, perfil_id):

    perfil = Perfil()

    if perfil_id == 1:
        perfil = Perfil('Rute Miliana', 'rute@gmail.com', '666-666', 'pitanguinha')
    if perfil_id == 2:
        perfil = Perfil('Jailson Mendes', 'dlccara@gmail.com', '666-666', 'Delicia')

    return render(request , 'perfil.html' , {'perfil' : perfil})
    ## terceiro parâmetro para a função render, que nada mais é do que um dicionário que contém a chave "perfil", que guarda o objeto perfil 
from django.urls import path
from . import views

urlpatterns = [
    #rota, função dentro do arquivo views, nome
    path('', views.index , name='index'), 
    path('perfis/<int:perfil_id>', views.exibir, name='exibir'),
]

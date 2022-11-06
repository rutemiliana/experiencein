from django.urls import path
from . import views

urlpatterns = [
    #rota, função dentro do arquivo views, nome
    path('', views.index , name='exibir'), 
    path('perfis/<int:perfil_id>', views.exibir, name='exibir'),
]

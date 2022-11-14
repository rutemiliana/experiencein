from django.db import models

# Create your models here.

class Perfil(models.Model): #Nome da tabela (ORM)
    #construtor, campos da tabela
    def __init__(self, nome='', email='', telefone='', nome_empresa=''):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.nome_empresa = nome_empresa


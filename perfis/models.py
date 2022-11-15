from django.db import models

# Create your models here.

class Perfil(models.Model): #Nome da tabela (ORM)
    # campos da tabela
    nome = models.CharField(max_length = 100, null = False)
    email = models.CharField(max_length = 100, null = False)
    telefone = models.CharField(max_length = 15, null = False)
    nome_empresa = models.CharField(max_length = 255, null = False)


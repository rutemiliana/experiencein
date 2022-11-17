# Experiencein
Python 3.10.7
Pip3
Django 2.2

# Create Project 
1. django-admin.py startproject xperiencein 
2. cd experiencein
3. python manage.py migrate
4. python manage.py runserver (http://localhost:8000)
5. python manage.py startapp perfis
6. Adicionar a aplicação 'perfis' na tupla INSTALLED_APPS no arquivo experiencein/experiencein/settings.py
7. Criar pagina perfil.html em experiencein/perfis/templates/
8. Atualizando arquivo models.py
9. python manage.py makemigrations
10. python manage.py migrate
11. Atualizando tamanho dos campos do Perfil
12. python manage.py makemigrations
13. python manage.py migrate
14. criar perfis no shell
15. adicionar função convidar em perfis/views.py
16. criar nova rota em perfils/urls.py
17. adicionar link para convite em templates/perfil 
18. adicionar método convidar na classe Perfil em perfis/models.py
19. criar classe convite em perfis/models.py

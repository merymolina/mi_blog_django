from django.contrib import admin
from .models import Post
admin.site.register(Post)
                               
python manage.py createsuperuser
python manage.py runserver
Ingresar a 127.0.0.1:8000/admin y crear varios post

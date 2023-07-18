from django.db import models
# importamos la clase abstracta de usuarios:
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField('Correo Electrónico', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    photo = models.ImageField(verbose_name='Foto de Perfil', upload_to='media/img/usuarios/')
    profile_profesional = models.TextField(verbose_name='Perfil Profesional', blank=True, null=True)
    country_origen = models.CharField(verbose_name='Pais', default='Colombia', max_length=45)
    ciudad_origen = models.CharField(verbose_name='Ciudad', default='Medellín', max_length=45)
    is_recruiter = models.BooleanField(default=False)
    created =models.DateTimeField(auto_now_add=True)
    modified =models.DateTimeField(auto_now=True)
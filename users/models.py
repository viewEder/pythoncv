from django.db import models
# importamos la clase abstracta de usuarios:
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField('Correo Electrónico', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    photo = models.ImageField(verbose_name='Foto de Perfil', upload_to='img/usuarios/')
    profile_profesional = models.TextField(verbose_name='Perfil Profesional', blank=True, null=True)
    resume_profesional = models.TextField(verbose_name='Resumen Profesional', blank=True, null=True)
    resume_skills = models.TextField(verbose_name='Resumen Habilidades', blank=True, null=True)
    occupation_job = models.CharField(verbose_name='Ocupacion', max_length=150, null=True, blank=True)
    linkedin = models.URLField(blank=True, verbose_name="LinkedIn")
    website = models.URLField(blank=True, verbose_name="Web Site")
    phone = models.CharField(verbose_name='Teléfono', max_length=20, null=True, blank=True)
    country_origen = models.CharField(verbose_name='Pais', default='Colombia', max_length=45)
    ciudad_origen = models.CharField(verbose_name='Ciudad', default='Medellín', max_length=45)
    birthday = models.DateField(verbose_name="Fecha de Nacimiento", null=True, blank=True)
    is_recruiter = models.BooleanField(default=False)
    created =models.DateTimeField(auto_now_add=True)
    modified =models.DateTimeField(auto_now=True)
from django.db import models

# Create your models here.
class User(models.Model):
    nombre = models.CharField (max_length=64)
    apellido = models.CharField (max_length=64)
    email = models.EmailField (blank= False)
    fecha_nac = models.DateField(null=True)
    dni = models.CharField (max_length=20)
    telefono = models.CharField (max_length=30, blank= True)
    
class Temas (models.Model):
    title = models.CharField (max_length=64)
    creador = models.CharField (max_length=64)

class post (models.Model):
    title = models.CharField (max_length=64)
    post = models.CharField (max_length=256)
    signature = models.CharField (max_length=64)
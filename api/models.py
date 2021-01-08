from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    uid= models.CharField(max_length=200)
    estado = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)


class Dispositivo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    modo=models.BooleanField(default=True)
    latitud=models.CharField(max_length=200)
    longitud=models.CharField(max_length=200)
    estado = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)


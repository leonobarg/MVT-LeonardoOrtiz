from django.db import models

# Create your models here.
class familia(models.Model):
    nombre=models.CharField(max_length=40)
    nacimiento=models.DateField()
    edad=models.IntegerField()
    parentesco=models.CharField(max_length=40)
    
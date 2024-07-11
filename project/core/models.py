import datetime
from django.db import models

# Create your models here.
class Gente(models.Model):

    nombre = models.CharField(max_length=100)
    lastChosen = models.DateField(default=datetime.date(2001, 1, 1))
    assignedDate = models.DateField(null=True, blank=True)
    def __str__(self) -> str:
        return self.nombre
    
class Mensaje(models.Model):
    msg = models.CharField(max_length=150)
    def __str__(self) -> str:
        return self.msg
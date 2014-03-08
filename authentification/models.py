from django.db import models

# Create your models here.

class Authentification (models.Model):
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=15)
    statut = models.BooleanField()

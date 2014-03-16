from django.db import models

# Create your models here.

class Authentification (models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)
    dateAjouter = models.DateField()
    statut = models.BooleanField()

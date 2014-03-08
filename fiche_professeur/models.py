from django.db import models
#from enregistrer_cours.models import Professeur

# Create your models here.
def content_file_name(instance, filename):
    return '/'.join(['content', instance.user.username, filename])


class Professeur (models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=10)
    email = models.EmailField()
    country = models.CharField(max_length=50)
    cv = models.FileField(upload_to=content_file_name)
    blog = models.URLField()

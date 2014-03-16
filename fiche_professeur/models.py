from authentification.models import Authentification
from django.db import models
#from enregistrer_cours.models import Professeur

# Create your models here.
def content_file_name(instance, filename):
    return '/'.join(['content', instance.user.username, filename])


class Professeur (models.Model):
    authen = models.ForeignKey(Authentification)
    sexe = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    cv = models.FileField(upload_to=content_file_name)
    blog = models.URLField()

from django.db import models
from descriptif_cours.models import TitreCours
from descriptif_cours.models import PlanCours
from descriptif_cours.models import Professeur

# Create your models here.
def content_file_name(instance, filename):
    return '/'.join(['content', instance.user.username, filename])

 
class Cours (models.Model):
    code_cours = models.IntegerField()
    professeur = models.ForeignKey(Professeur)
    titre_cours = models.ForeignKey(TitreCours)
    planCours = models.ForeignKey(PlanCours)
    credits = models.IntegerField()
    pre_requis = models.TextField()
    lieu = models.CharField(max_length=50)
    public_cible = models.CharField(max_length=20)
    format = models.CharField(max_length=20)

class Programme (models.Model):
    domaine = models.CharField(max_length=10)
    mention = models.CharField(max_length=20)
    specialite= models.CharField(max_length=20)
    typeCours = models.CharField(max_length=10)
    langue = models.CharField(max_length=10)
    cours = models.ManyToManyField(Cours)


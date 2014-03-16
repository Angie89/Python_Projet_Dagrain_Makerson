from django.db import models

# Create your models here.
#from enregistrer_cours.models import Cours, PlanCours, Professeur,TitreCours

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


class TitreCours(models.Model):
    grade = models.CharField(max_length=10)
    etablissement = models.CharField(max_length=50, default='ESIH')
    semestre = models.CharField(max_length=10)
    nomCours = models.CharField(max_length=20)

class PlanCours(models.Model):
    objectifs = models.TextField()
    descriptionCours = models.TextField()
    Ressources = models.TextField()
    evaluations = models.TextField()

# class Cours (models.Model):
#     code_cours = models.IntegerField()
#     professeur = models.ForeignKey(Professeur)
#     titre_cours = models.ForeignKey(TitreCours)
#     planCours = models.ForeignKey(PlanCours)
#     credits = models.IntegerField()
#     pre_requis = models.TextField()
#     lieu = models.CharField(max_length=50)
#     public_cible = models.CharField(max_length=20)
#     format = models.CharField(max_length=20)

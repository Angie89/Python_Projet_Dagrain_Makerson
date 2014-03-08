from GestionESIH.models import Utilisateurs
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from GestionESIH.models import Utilisateurs

import datetime

# Create your views here.
# def admin(request):
#     utilisa=Utilisateurs.objects.all()
#     context = {}
#     html = get_template("admin.html")
#     admin= html.render(Context(context))
#     return HttpResponse(admin)

def dat(request):
    #list=
    d=datetime.datetime.now()
    return render(request, 'exDjango/admin.html', {'current_date': d})

def scolarite(request):
    context = {}
    html = get_template("tableau.html")
    tabl= html.render(Context(context))
    return HttpResponse(tabl)

def users(request):
    context = {}
    html = get_template("users.html")
    users= html.render(Context(context))
    return HttpResponse(users)

def ajouterUser(request):
    try:
        user = Utilisateurs(nom=request.POST['Nom'], prenom=request.POST['Prenom'], email=request.POST['mail'], dateAjouter=datetime.datetime.now())
        user.save()
        pass
    except KeyError:
        pass
    context={}
    html=get_template('users.html')
    page=html.render(Context(context))
    return HttpResponse(page)
    #return render(request,'enregistrerCours.html', locals())

# def insertProgramme(request):
#     try:
#
#     except KeyError:
#         pass
#     return render(request,'enregistrerCours.html', locals())
#def information(request, cours, prof):
    #return render(request, 'page.html', locals())
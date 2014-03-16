from authentification.models import Authentification
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
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
    return render(request, 'exDjango/admin.html', {'current_date': d,'userid':request.session['userid']})

def scolarite(request):
    context = {'userid':request.session['userid']}
    html = get_template("tableau.html")
    tabl= html.render(Context(context))
    return HttpResponse(tabl)


def users(request):
    context = {'userid':request.session['userid']}
    html = get_template("users.html")
    users= html.render(Context(context))
    return HttpResponse(users)


def ajouterUser(request):
    try:
        droit = False
        if request.POST['droit'].__eq__("Administrateur"):
            droit = True
        password = "{}{}2014".format(request.POST['Prenom'][0],request.POST['Nom'][0])
        user = Authentification(password=password,statut=droit,nom=request.POST['Nom'], prenom=request.POST['Prenom'], email=request.POST['mail'], dateAjouter=datetime.datetime.now())
        user.save()
        pass
    except KeyError:
        pass
    context={'userid':request.session['userid']}
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
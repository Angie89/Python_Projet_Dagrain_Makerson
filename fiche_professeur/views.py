from authentification.models import Authentification
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

# Create your views here.
from fiche_professeur.models import Professeur


def ficheProfesseuradmin(request):
    context = {'userid':request.session['userid']}
    html = get_template("ficheProfesseuradmin.html")
    fiche = html.render(Context(context))
    return HttpResponse(fiche)


def ficheProfesseurprof(request):
    context = {'userid':request.session['userid']}
    html = get_template("ficheProfesseurprof.html")
    fiche = html.render(Context(context))
    return HttpResponse(fiche)

def professeur(request):
    context = {'userid':request.session['userid']}
    html = get_template("Professeur.html")
    pro = html.render(Context(context))
    return HttpResponse(pro)

def modifierProf(request, id):
    try:
        prof = Professeur.objects.get(id=id)
        pass
    except:
        pass
    context = {'userid':request.session['userid']}
    html = get_template('modifierProf.html')
    page = html.render(Context(context))
    return HttpResponse(page)

def deleteProf(request, clef):
    try:
        recupereClef = Authentification.objects.get(id=clef)
        recupereClef.delete()
        pass
    except:
        pass
    return redirect("/admin/")
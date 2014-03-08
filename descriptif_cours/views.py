from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from descriptif_cours.models import TitreCours

# Create your views here.
from enregistrer_cours.models import PlanCours


def descriptifCours(request):
    codeCours = TitreCours.objects.all()
    context = {}
    html = get_template("descriptifCours.html")
    page=html.render(Context({'cod':codeCours}))
    return HttpResponse(page)

def Objectives(request):
    context = {}
    html = get_template("Objectives.html")
    ob = html.render(Context(context))
    return HttpResponse(ob)

def Description(request):
    context = {}
    html = get_template("Description.html")
    descrip = html.render(Context(context))
    return HttpResponse(descrip)

def Ressources(request):
    context = {}
    html = get_template("Ressources.html")
    res = html.render(Context(context))
    return HttpResponse(res)

def Evaluations(request):
    context = {}
    html = get_template("Evaluations.html")
    evalu = html.render(Context(context))
    return HttpResponse(evalu)

def insertDescription(request):
    try:
        plancours = PlanCours(objectifs=request.POST['objectifs'], Ressources=request.POST['ressources'], evaluations=request.POST['evaluations'], descriptionCours=request.POST['description'])
        plancours.save()
    except KeyError:
        pass
    return render(request,'', locals())



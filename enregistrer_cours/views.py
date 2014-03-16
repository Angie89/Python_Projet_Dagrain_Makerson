from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

# Create your views here.
from enregistrer_cours.models import TitreCours, Programme


def enregistrerCours(request):
    context = {'userid':request.session['userid']}
    html = get_template("enregistrerCours.html")
    cours = html.render(Context(context))
    return HttpResponse(cours)


def insertTitre(request):
    try:
        titrecours = TitreCours(grade=request.POST['Grade'], etablissement=request.POST['etablissment'],
                                semestre=request.POST['Semestre'], nomCours=request.POST['cours'])
        titrecours.save()
        programme = Programme(domaine=request.POST['domaine'], mention=request.POST['mention'],
                              typeCours=request.POST['typecours'], specialite=request.POST['Specialite'],
                              langue=request.POST['langue'])
        programme.save()
        pass
    except KeyError:
        pass
    context = {'userid':request.session['userid']}
    html = get_template('enregistrerCours.html')
    page = html.render(Context(context))
    return HttpResponse(page)
    #return render(request,'enregistrerCours.html', locals())

# def insertProgramme(request):
#     try:
#
#     except KeyError:
#         pass
#     return render(request,'enregistrerCours.html', locals())

#
# def listeCours(request):
#     rec= TitreCours.objects.all()
#     recpro= Programme.objects.all()
#     context = {}
#     html = get_template('listingTitreCours.html')
#     page = html.render(Context(context))
#     return HttpResponse(page)

def recupercode(request,id):
    TitreCours.objects.get(id=id).delete()
    Programme.objects.get(id=id).delete()
    return HttpResponse(id)


def filtrage(request):
    #try:
    recuperate = TitreCours.objects.all()
    recuperate1 = Programme.objects.all()
      #  pass
    #except:
     #   pass

    context = {"recuperate":recuperate,"recuperate1":recuperate1}
    html = get_template('listingTitreCours.html')
    page = html.render(Context(context))
    return HttpResponse(page)

# def supprimer(request, clef):
#     try:
#         recupereClef = TitreCours.objects.get(id=clef)
#         recupereClef.delete()
#         pass
#     except:
#         pass
#     return redirect("/listingTitreCours/")


def modifier(request, id):
    try:
        code = TitreCours.objects.get(id=id)
        pass
    except:
        pass
    context = {'userid':request.session['userid']}
    html = get_template('modificationCode.html')
    page = html.render(Context(context))
    return HttpResponse(page)
    #return render(request, 'modificationCode.html', locals())


def modifierProgramme(request, id):
    try:
        programme = Programme.objects.get(id=id)
        pass
    except:
        pass
    context = {'userid':request.session['userid']}
    html = get_template('modificationProgramme.html')
    page = html.render(Context(context))
    return HttpResponse(page)
    #return render(request, 'modificationProgramme.html', locals())





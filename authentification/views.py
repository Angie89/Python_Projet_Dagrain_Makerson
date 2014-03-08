from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from authentification.models import Authentification
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from GestionESIH.models import Utilisateurs



# Create your views here.
def login (request):
    context = {}
    list = Authentification.objects.all()
    if len(list) == 0:
        auth = Authentification(username="admin@admin.com",password="password",statut=True)
        auth.save()

    try:
        username = request.POST['mail']
        password = request.POST['password']
        user = Authentification.objects.filter(username=username,password=password)
        for personne in list:
            if personne.username==username and personne.password==password:
                request.session['userid'] = username
                request.session['status'] = personne.statut
                context['userid']=request.session['userid']
                context['status']=request.session['status']
                if personne.statut == True:
                    return redirect('/admin/', context_instance=request)
                else:
                    return redirect('/professeur/', context_instance=request)
        else:
            context['error'] = 'Username ou password incorrect'


    except KeyError:
        pass
    html = get_template("authen.html")
    page = html.render(Context(context))
    return HttpResponse(page)

def admin(request):
    context = {}
    utilisa=Utilisateurs.objects.all()
    context['userid']=request.session['userid']
    html = get_template("admin.html")
    page=html.render(Context({'user':utilisa}))
    return HttpResponse(page)

def logout(request):

    try:
        del request.session['userid']
        server = request.get_host()
        return redirect(server)


    except KeyError:
        pass
    return redirect(reverse(login))
# def logout(request):
#      logout(request)
#      return redirect(reverse(login))



from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.contrib import admin
from authentification.views import login, admin, logout
from enregistrer_cours.views import enregistrerCours
from fiche_professeur.views import ficheProfesseur, modifierProf, deleteProf, professeur
from descriptif_cours.views import descriptifCours, Objectives, Description, Ressources, Evaluations
from enregistrer_cours.views import insertTitre, filtrage, modifier, modifierProgramme,recupercode
from GestionESIH.views import ajouterUser, users, scolarite

#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'exDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
   # url(r'^info/(?P<cours>\d+)/(?P<prof>\d+)/$','GestionESIH.views.information'),
    url(r'^login/$',login),
    url(r'^logout', logout),
    url(r'^admin/$',admin),
     url(r'^users/$',ajouterUser),
    url(r'^enregistrerCours/$', insertTitre),
    url(r'^ficheProfesseur/$', ficheProfesseur),
     url(r'^professeur/$', professeur),
    url(r'^descriptifCours/$', descriptifCours),
    url(r'^Objectives/$',Objectives),
    url(r'^Description/$',Description),
    url(r'^Ressources/$',Ressources),
    url(r'^Evaluations/$',Evaluations),
    url(r'^scolarite/$',scolarite),
    url(r'^filtrage/$', filtrage),
    url(r'^mod/(\d+)/$',modifier),
    url(r'^modifierProf/(\d+)/$', modifierProf),
    url(r'^deleteProf/(\d+)/$',deleteProf),
    url(r'^modProgramme/(\d+)/$',modifierProgramme),
    url(r'^recupercode/(\d+)/$',recupercode),
)

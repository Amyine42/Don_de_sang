from django.urls import path
from . import views

urlpatterns = [
    path("accueil/",views.articleAccueil),
    path("pourquoi/",views.desc),
    path('qui/',views.qui),
    path('ou-donner/',views.oudonner),
    path('contact/',views.contact),
    path('survey/',views.survey),
]
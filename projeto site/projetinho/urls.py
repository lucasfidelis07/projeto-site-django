from django.contrib import admin
from django.urls import path
from posts.views import listar_coisas, detalhar_processadores, processadores, memorias, video, mae

urlpatterns = [
    path('principal/', listar_coisas),
    path('processadores/<int:id>/', detalhar_processadores),
    path('processadores/', processadores),
    path('memorias/', memorias),
    path('placas_de_video/', video),
    path('placas_mae/', mae)
]


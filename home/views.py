from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return HttpResponse("<h1>Page d'accueil</h1>")

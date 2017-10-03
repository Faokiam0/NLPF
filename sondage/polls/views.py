from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Sinon y a la matrice des flux à remplir.")
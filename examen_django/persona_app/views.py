from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona



# Create your views here.
def persona_list(request):
    Personne = Persona.objects.filter(available=True)
    return HttpResponse(Persona.first_name)

def persona_details(request, id):
    return HttpResponse(f"Détails d'une personne {id}")

def persona_create(request):
    return HttpResponse("Creation d'une personne")

def persona_update(request, id):
    return HttpResponse(f"Update d'une personne : {id}")

def persona_delete(request, id):
    return HttpResponse(f"Delete d'une personne : {id}")
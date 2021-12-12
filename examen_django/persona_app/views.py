from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona

# Create your views here.
def persona_list(request):
    personne = Persona.objects.all().order_by('-id')
    context = {'personne':personne}
    # return render(request,"",context)
    return render(request,'persona_app\liste_template.html', context)
    # return HttpResponse(personne)

def persona_details(request, id):
    personne = Persona.objects.get(pk=id)
    context={}
    return HttpResponse(personne)

def persona_create(request):
    return HttpResponse("Creation d'une personne")

def persona_update(request, id):
    return HttpResponse(f"Update d'une personne : {id}")

def persona_delete(request, id):
    return HttpResponse(f"Delete d'une personne : {id}")


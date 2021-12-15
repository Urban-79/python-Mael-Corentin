from types import new_class
from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona
import requests

# Create your views here.
def persona_list(request):
    personne = Persona.objects.all().order_by('-id')
    context = {'personne':personne}
    # return render(request,"",context)
    return render(request,'persona_app\list_template.html', context)
    # return HttpResponse(personne)

def persona_details(request, id):
    personne = Persona.objects.get(id=id)
    context={'personne':personne}
    return render(request,'persona_app\details_template.html', context)

def persona_generate(request):
    url="https://randomuser.me/api?nat=fr>"
    personne = requests.get(url)
    context={'personne':personne}
    return render(request,'persona_app\create_template.html', context)
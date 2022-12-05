from django.shortcuts import render
from main.models import Projetos


# Create your views here.

def index (request):
    projetos = Projetos.objects.all()
    return render(request, 'portfolio/index.html', {'projetos': projetos})



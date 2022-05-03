from django.shortcuts import render
import random
from django.http import HttpResponse
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'PortfolioApp/home.html', {'projects':projects})

from django.shortcuts import render
from django.http import HttpResponse
from . models import Department

def index(request):
    department=Department.objects.all()
    return render(request,"index.html",{"department":department})

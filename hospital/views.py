from django.shortcuts import render
from django.http import HttpResponse
from . models import Department, Doctor

def index(request):
    department=Department.objects.all()
    doctor=Doctor.objects.all()
    context = {
        "department":department,
        "doctor":doctor
    }
    return render(request,"index.html",context)

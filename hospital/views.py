from django.shortcuts import render
from django.http import HttpResponse
from . models import Department, Doctor
from . forms import BookingForm

def index(request):
    department=Department.objects.all()
    doctor=Doctor.objects.all()
    form=BookingForm()
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Booking Success")
    context = {
        "department":department,
        "doctor":doctor,
        "form":form
    }
    return render(request,"index.html",context)

from django.shortcuts import render
from . import models

def list_patients(request):
    return render(request, 'office/list.html', context={'patients':models.Patient.objects.all()})
    

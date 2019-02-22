from django.http  import HttpResponse 
from django.shortcuts import render

# Create your views here.
def proff(request):
    return render(request, 'landing.html')

def proj(request):
    return render (request,'projects.html' )

def skill(request):
    return render(request, 'skills.html')

def contact(request):
    return render (request,'contacts.html' )


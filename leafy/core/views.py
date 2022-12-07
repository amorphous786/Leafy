from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    print("Philospher Stone")
    print("tsukitsukitsukitsukitsukitsuki")
    
    return HttpResponse("<h1>Did you get Peanuts?</h1>\ntsukitsukitsukitsukitsukitsuki")
    
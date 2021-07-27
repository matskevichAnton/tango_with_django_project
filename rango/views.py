from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    forward = "<a href='/rango/about/'>About</a>"
    return HttpResponse("Rango says hey there partner!" + forward)

# Create your views here.
def about(request):
    backward = "<a href='/rango/'>back</a>"
    return HttpResponse("Rango says here is the about page!" + backward)
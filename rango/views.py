from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': 'crunchy, creamy, cookie, candy, cupcake!'}

    return render(request, 'rango/index.html', context=context_dict)
# Create your views here.
def about(request):
        context_dict = {'name': 'Anton Matskevich'}

        return render(request, 'rango/about.html', context=context_dict)
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request, *args, **kwargs):
    context = {
            'text':"Texto del desarrollador",
            'number':12,
            }
    return render(request, "home.html", context)

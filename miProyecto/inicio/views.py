from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request, *args, **kwargs):
    return render(request, "home.html", {})

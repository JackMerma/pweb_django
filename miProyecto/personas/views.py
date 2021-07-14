from django.shortcuts import render
from .models import  Persona
from .forms import PersonaForm, RawPersonaForm

# Create your views here.
def personaTestView(request):
    obj=Persona.objects.get(id=1)
    context={
            'objeto':obj,
            }
    print(context)
    return render(request, 'descripcion.html', context)

def personaCreateView(request):
    form = PersonaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=PersonaForm()

    context={
            'form':form
            }
    return render(request, 'personasCreate.html', context)

def personaAnotherCreateView(request):
    form=RawPersonaForm(request.POST)
    context={
        'form':form
    }
    return render(request, 'personasCreate.html', context)


def searchForHelp(request):
    return render(request, 'search.html', {})

from django.shortcuts import render, get_object_or_404
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
    #obj=Persona.objects.get(id=2)
    #form=PersonaForm(request.POST or None, instance=obj)
    initialValues={
        'nombres':'sin Nombre'
    }

    form=PersonaForm(request.POST or None, initial=initialValues)
    #form = PersonaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=PersonaForm()

    context={
            'form':form
            }
    return render(request, 'personasCreate.html', context)

def personaAnotherCreateView(request):
    #form=RawPersonaForm()
    form=PersonaForm()
    if(request.method=='POST'):
        #form=RawPersonaForm(request.POST)
        form=PersonaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Persona.objects.create(**form.cleaned_data)
        else:
            print(form.errors)

    context={
        'form':form
    }
    return render(request, 'personasCreate.html', context)


def searchForHelp(request):
    return render(request, 'search.html', {})

def personasShowObject(request, myID):
    obj=get_object_or_404(Persona,id=myID)
    context={
        'objeto':obj
    }
    return render(request, 'descripcion.html', context)

def personasDeleteView(request, myID):
    obj=get_object_or_404(Persona,id=myID)
    if request.method=='POST':
        print('lo borro')
        obj.delete()
    context={
        'objeto':obj
    }
    return render(request, 'personasBorrar.html', context)

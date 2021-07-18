from django.shortcuts import render, get_object_or_404, redirect
from .models import  Persona
from .forms import PersonaForm, RawPersonaForm
from django.urls import reverse_lazy

from django.views import View
from django.http import HttpResponse, JsonResponse

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

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
        return redirect('../../')
    context={
        'objeto':obj
    }
    return render(request, 'personasBorrar.html', context)


def personasListView(request):
    queryset=Persona.objects.all()
    context={
        'objectList':queryset
    }
    return render(request, 'personasLista.html', context)


#VISTAS como clases

class PersonaDetailView(DetailView):
    model = Persona

class PersonaListView(ListView):
    model = Persona
    #queryset = Persona.objects.filter(nombres = 'Jackson')

class PersonaCreateView(CreateView):
    model = Persona
    fields = [
        'nombres',
        'apellidos',
        'edad',
        'donador',
    ]
    template_name_suffix = '_create'

class PersonaUpdateView(UpdateView):
    model = Persona
    fields = [
        'nombres',
        'apellidos',
        'edad',
        'donador',
    ]
    template_name_suffix = '_update'

class PersonaDeleteView(DeleteView):
    model = Persona
    #template_name_suffix = '_delete'
    success_url = reverse_lazy('personas:persona-list')

class PersonaQueryView(View):
    def get(self, request, *args, **kwargs):
        queryset = Persona.objects
        return JsonResponse(list(queryset.values()), safe = False)
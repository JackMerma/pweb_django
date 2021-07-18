from django.urls import path
from personas.views import (
    #personaTestView, 
    #personaCreateView, 
    #personasShowObject,
    personasDeleteView,
    #personasListView,
    PersonaListView,
    PersonaDetailView,
    PersonaCreateView,
    PersonaUpdateView,
    )
app_name='personas'
urlpatterns = [
    path('<int:myID>/delete/', personasDeleteView, name='deleting'),
    path('', PersonaListView.as_view(), name='persona-list'),
    path('<int:pk>/', PersonaDetailView.as_view(), name='persona-detail'),
    path('create/', PersonaCreateView.as_view(), name='persona-create'),
    path('<int:pk>/update/', PersonaUpdateView.as_view(), name='persona-update'),

    #path('agregar/', personaCreateView, name="create"),
    #path('<int:myID>/', personasShowObject, name='browsing'),
    #path('', personasListView, name='listing')
    #path('people/', personaTestView, name="testViewPersonas"),
    #path('otroAgregar', personaAnotherCreateView, name='OtroAgregarPersonas'),
    #path('search', searchForHelp, name="buscar"),
]

from django.urls import path
from personas.views import (
    personaTestView, 
    personaCreateView, 
    personasShowObject,
    personasDeleteView,
    personasListView,
    )
app_name='personas'
urlpatterns = [
    path('agregar/', personaCreateView, name="create"),
    path('<int:myID>/', personasShowObject, name='browsing'),
    path('<int:myID>/delete/', personasDeleteView, name='deleting'),
    path('', personasListView, name='listing')

    #path('people/', personaTestView, name="testViewPersonas"),
    #path('otroAgregar', personaAnotherCreateView, name='OtroAgregarPersonas'),
    #path('search', searchForHelp, name="buscar"),
]

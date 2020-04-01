from .views import lista_animal, cadastro_animal
from django.urls import path

urlpatterns = [
    path('', lista_animal),
    path('cadastro-animal', cadastro_animal)
]

from .views import perfil, alterar, informacoes, excluir_conta, excluir_animal
from django.urls import path

urlpatterns = [
    path('animais', perfil, name='animais'),
    path('alterar-informacoes/<int:id>/', alterar, name='alterar-informacoes'),
    path('informacoes-pessoais', informacoes, name='informacoes-pessoais'),
    path('excluir-conta/<int:id>/', excluir_conta, name='excluir-conta'),
    path('excluir-animal/<int:id>/', excluir_animal, name='excluir-animal'),
]

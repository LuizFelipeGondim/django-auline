from .views import perfil, alterar, informacoes, excluir_conta
from django.urls import path

urlpatterns = [
    path('animais', perfil, name='animais'),
    path('alterar-informacoes/<int:id>/', alterar, name='alterar-informacoes'),
    path('informacoes-pessoais', informacoes, name='informacoes-pessoais'),
    path('excluir-conta/<int:id>/', excluir_conta, name='excluir-conta'),
]

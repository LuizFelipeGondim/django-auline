from .views import lista_pub
from django.urls import path

urlpatterns = [
    path('', lista_pub),
]

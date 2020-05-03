from .views import contato
from django.urls import path

urlpatterns = [
    path('', contato, name='contato'),
]

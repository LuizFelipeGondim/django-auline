from .views import cadastro
from django.conf.urls import url

urlpatterns = [
    url('cadastro', cadastro),
]
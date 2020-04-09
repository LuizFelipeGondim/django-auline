from .views import cadastro, login, logout_view
from django.conf.urls import url

urlpatterns = [
    url('cadastro', cadastro),
    url('login', login),
    url('logout', logout_view)
    
]
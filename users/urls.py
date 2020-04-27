from .views import cadastro, login, logout_view
from django.urls import path

urlpatterns = [
    path('cadastro/', cadastro, name='cadastro'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
]
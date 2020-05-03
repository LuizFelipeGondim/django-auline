from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('publicacoes.urls')),
    path('accounts/', include('users.urls'), name='accounts'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('perfil/', include('perfis.urls'), name='perfil'),
    path('entre-em-contato/', include('contato.urls'), name='entre-em-contato'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include
# Importações para servir arquivos estáticos em desenvolvimento
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # Para login/logout
    path('register/', include('usuarios.urls')), # Para registro
    path('', include('producao.urls')), # Para as URLs da sua app 'producao'
]

# SOMENTE em modo DEBUG, o Django serve arquivos estáticos e de mídia
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Se você também tiver arquivos de mídia (uploads de usuários)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
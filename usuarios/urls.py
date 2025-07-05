from django.urls import path
from . import views

app_name = 'usuarios' # Opcional, mas boa prática para namespace de URLs

urlpatterns = [
    # path('alguma_url/', views.alguma_view, name='alguma_nome_url'),
    # ... suas URLs de usuário aqui (ex: path('cadastro/', views.register, name='register'))
]
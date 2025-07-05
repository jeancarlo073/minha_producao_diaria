# minha_producao_diaria/producao/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('adicionar/', views.adicionar_producao, name='adicionar_producao'),
    path('listar/', views.listar_producoes, name='listar_producoes'),
    path('editar/<int:pk>/', views.editar_producao, name='editar_producao'),
    path('excluir/<int:pk>/', views.excluir_producao, name='excluir_producao'),
    path('register/', views.register, name='register'), # <-- Nova URL para registro
]
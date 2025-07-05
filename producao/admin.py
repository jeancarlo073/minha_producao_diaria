# minha_producao_diaria/producao/admin.py

from django.contrib import admin
from .models import ProducaoDiaria # Importa o modelo que acabamos de criar

# Registra o modelo ProducaoDiaria para que ele apareça no painel de administração
admin.site.register(ProducaoDiaria)
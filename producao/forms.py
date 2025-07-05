# minha_producao_diaria/producao/forms.py

from django import forms
from .models import ProducaoDiaria
from django.contrib.auth.forms import UserCreationForm, UserChangeForm # Importe estes para o registro de usuário
from django.contrib.auth.models import User # Importe o modelo User

class ProducaoDiariaForm(forms.ModelForm):
    class Meta:
        model = ProducaoDiaria
        # Certifique-se de que todos os campos estão aqui
        fields = [
            'data', 'bairro', 'ciclo_ano', 'nome_responsavel',
            'numero_quarteirao', 'semana_epidemiologica',
            'residencia', 'comercio', 'terreno_baldios',
            'ponto_estrategico', 'outros', 'eliminados',
            'recusas', 'fechados', 'recuperados'
        ]
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }

# Novo Formulário de Registro de Usuário
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',) # Adiciona 'email' aos campos de registro
        # Você pode adicionar mais campos aqui se quiser, como 'first_name', 'last_name'
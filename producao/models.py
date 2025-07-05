# minha_producao_diaria/producao/models.py

from django.db import models
from django.contrib.auth.models import User # Importar o modelo User

class ProducaoDiaria(models.Model):
    # Adicione o campo user aqui
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='producoes_diarias')

    data = models.DateField()
    bairro = models.CharField(max_length=100)
    ciclo_ano = models.CharField(max_length=100) # Mantive como CharField, se for só ano, pode ser IntegerField
    nome_responsavel = models.CharField(max_length=100) # Este campo pode ser removido depois, se o 'user' for o suficiente
    numero_quarteirao = models.IntegerField()
    semana_epidemiologica = models.IntegerField()

    # Tipos de Imóveis (detalhes da produção)
    residencia = models.IntegerField(default=0)
    comercio = models.IntegerField(default=0)
    terreno_baldios = models.IntegerField(default=0)
    ponto_estrategico = models.IntegerField(default=0)
    outros = models.IntegerField(default=0)

    # Resultados
    eliminados = models.IntegerField(default=0)
    recusas = models.IntegerField(default=0)
    fechados = models.IntegerField(default=0)
    recuperados = models.IntegerField(default=0) # Recuperados de visitas anteriores

    data_registro = models.DateTimeField(auto_now_add=True) # Data e hora que o registro foi criado

    def __str__(self):
        return f"Produção de {self.data} - {self.bairro} ({self.user.username})"

    class Meta:
        verbose_name = "Produção Diária"
        verbose_name_plural = "Produções Diárias"
        ordering = ['-data', 'bairro'] # Ordenar por data decrescente e bairro
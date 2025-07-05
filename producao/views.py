# minha_producao_diaria/producao/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse # Importação mantida por segurança, mesmo que não usada diretamente agora
from .forms import ProducaoDiariaForm, CustomUserCreationForm # Importe ProducaoDiariaForm e CustomUserCreationForm
from django.contrib import messages
from .models import ProducaoDiaria
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login # Importe a função login para logar o usuário após o registro

# -----------------------------------------------------------
# Views de Autenticação e Dashboard
# -----------------------------------------------------------

@login_required
def dashboard(request):
    """
    Renderiza a página do dashboard com opções para o usuário.
    Esta será a nova página inicial após o login.
    """
    return render(request, 'producao/dashboard.html')


def register(request):
    """
    Permite que novos usuários se registrem no sistema.
    Faz o login do usuário automaticamente após o registro bem-sucedido.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Faz o login do usuário automaticamente
            messages.success(request, 'Conta criada com sucesso! Você foi logado automaticamente.')
            return redirect('home') # Redireciona para o dashboard
        else:
            # Se o formulário não for válido, os erros serão exibidos no template
            messages.error(request, 'Erro ao criar a conta. Por favor, verifique os dados.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'producao/register.html', {'form': form})


# -----------------------------------------------------------
# Views de CRUD para Produção Diária
# -----------------------------------------------------------

@login_required
def adicionar_producao(request):
    """
    Esta view exibe um formulário para adicionar uma nova produção
    e processa o envio do formulário, associando a produção ao usuário logado.
    """
    if request.method == 'POST':
        form = ProducaoDiariaForm(request.POST)
        if form.is_valid():
            # Não salva ainda no banco de dados, apenas cria o objeto em memória
            producao = form.save(commit=False)
            # Associa a produção ao usuário atualmente logado
            producao.user = request.user
            # Agora sim, salva a produção no banco de dados
            producao.save()
            messages.success(request, 'Dados salvos no banco de dados com sucesso!')
            return redirect('adicionar_producao') # Pode redirecionar para a lista ou para o dashboard
        else:
            messages.error(request, 'Por favor, corrija os erros no formulário.')
    else:
        form = ProducaoDiariaForm()

    return render(request, 'producao/adicionar_producao.html', {'form': form})


@login_required
def listar_producoes(request):
    """
    Esta view lista todas as produções diárias DO USUÁRIO LOGADO,
    com filtros opcionais de ciclo/ano e semana epidemiológica.
    """
    # Filtra as produções para mostrar APENAS as do usuário logado
    producoes = ProducaoDiaria.objects.filter(user=request.user)

    filtro_ciclo_ano = request.GET.get('ciclo_ano')
    filtro_semana_epidemiologica = request.GET.get('semana_epidemiologica')

    if filtro_ciclo_ano:
        producoes = producoes.filter(ciclo_ano__icontains=filtro_ciclo_ano)

    if filtro_semana_epidemiologica:
        producoes = producoes.filter(semana_epidemiologica__icontains=filtro_semana_epidemiologica)

    producoes = producoes.order_by('-data') # Garante ordenação consistente

    context = {
        'producoes': producoes,
        'filtro_ciclo_ano': filtro_ciclo_ano,
        'filtro_semana_epidemiologica': filtro_semana_epidemiologica,
    }
    return render(request, 'producao/listar_producoes.html', context)


@login_required
def editar_producao(request, pk):
    """
    Esta view permite editar uma produção diária existente.
    Apenas o usuário proprietário da produção pode editá-la.
    """
    # Garante que apenas o proprietário da produção pode acessá-la para edição
    producao = get_object_or_404(ProducaoDiaria, pk=pk, user=request.user)

    if request.method == 'POST':
        form = ProducaoDiariaForm(request.POST, instance=producao)
        if form.is_valid():
            form.save() # O user já está associado, então pode salvar diretamente
            messages.success(request, 'Produção atualizada com sucesso!')
            return redirect('listar_producoes')
        else:
            messages.error(request, 'Por favor, corrija os erros no formulário.')
    else:
        form = ProducaoDiariaForm(instance=producao)

    context = {
        'form': form,
        'producao': producao,
    }
    return render(request, 'producao/editar_producao.html', context)


@login_required
def excluir_producao(request, pk):
    """
    Esta view permite excluir uma produção diária.
    Apenas o usuário proprietário da produção pode excluí-la.
    Lida com a exibição da página de confirmação (GET) e com a exclusão real (POST).
    """
    # Garante que apenas o proprietário da produção pode acessá-la para exclusão
    producao = get_object_or_404(ProducaoDiaria, pk=pk, user=request.user)

    if request.method == 'POST':
        producao.delete()
        messages.success(request, 'Produção excluída com sucesso!')
        return redirect('listar_producoes')
    # Se for uma requisição GET, renderiza a página de confirmação
    return render(request, 'producao/confirmar_exclusao.html', {'producao': producao})


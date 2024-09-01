from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .forms import PacienteForm

def cadastro_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listagem_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/cadastro.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Paciente

def listagem_pacientes(request):
    search_query = request.GET.get('search', '')
    if search_query:
        # Filtra pacientes com base na pesquisa
        pacientes = Paciente.objects.filter(nome__icontains=search_query)
    else:
        pacientes = Paciente.objects.all()

    # Se apenas um paciente for encontrado, exibe o detalhe dele
    if pacientes.count() == 1:
        paciente = pacientes.first()
        return render(request, 'pacientes/paciente_detalhe.html', {'paciente': paciente})

    return render(request, 'pacientes/listagem.html', {'pacientes': pacientes})


def index(request):
    return render(request, 'pacientes/index.html')

def atualizar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('listagem_pacientes')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'pacientes/atualizar.html', {'form': form, 'paciente': paciente})
    
def excluir_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('listagem_pacientes')
    return render(request, 'pacientes/excluir.html', {'paciente': paciente})


def listar_paciente(request):
    search_query = request.GET.get('search', '')
    if search_query:
        # Filtra pacientes com base na pesquisa
        pacientes = Paciente.objects.filter(nome__icontains=search_query)
    else:
        pacientes = Paciente.objects.all()

    # Se apenas um paciente for encontrado, exibe o detalhe dele
    if pacientes.count() == 1:
        paciente = pacientes.first()
        return render(request, 'pacientes/paciente_detalhe.html', {'paciente': paciente})

    return render(request, 'pacientes/listagem.html', {'pacientes': pacientes})

from itertools import product
from django.shortcuts import render, redirect
from empresa.models import Funcionario
from .forms import FuncionarioForm


def lista_funcionarios(request):
    funcionarios = Funcionario.objetos.all()
    return render(request, 'lista.html', {'funcionarios':funcionarios})


def cadastrar_funcionario(request):
    formulario = FuncionarioForm(request.POST or None)

    if formulario.is_valid():
        formulario.save()
        return redirect('lista_funcionarios')

    return render(request, 'cadastrar.html', {'formulario':formulario})


def atualizar_funcionario(request, id):
    funcionario = Funcionario.objetos.get(id=id)
    formulario = FuncionarioForm(request.POST or None, instance= funcionario)

    if formulario.is_valid():
        formulario.save()
        return redirect('lista_funcionarios')

    return render(request, 'cadastrar.html', {'formulario':formulario, 'funcionario':funcionario})


def excluir_funcionario(request, id):
    funcionario = Funcionario.objetos.get(id=id)

    if request.method == "POST":
        funcionario.delete()
        return redirect('lista_funcionarios')

    return render(request, 'excluir.html', {'funcionario':funcionario})


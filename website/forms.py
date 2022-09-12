from dataclasses import field
from django import forms
from empresa.models import Funcionario


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome','sobrenome','cpf','tempo_de_servico','remuneracao']
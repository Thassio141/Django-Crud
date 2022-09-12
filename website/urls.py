from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_funcionarios, name='lista_funcionarios'),
    path('cadastrar/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('atualizar/<int:id>/', views.atualizar_funcionario, name='atualizar_funcionario'),
    path('excluir/<int:id>/', views.excluir_funcionario, name='excluir_funcionario'),
]
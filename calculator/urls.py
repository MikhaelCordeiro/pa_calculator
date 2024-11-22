from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculadora_pa, name='calculadora_pa'),  # Rota da página inicial
    # Outras rotas aqui...
]

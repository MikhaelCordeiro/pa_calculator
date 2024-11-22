from django.urls import path
from . import views

urlpatterns = [
    path('calculadora/', views.calculadora_pa, name='calculadora'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_lojas, name='listar_lojas'),
]

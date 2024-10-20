from django.urls import path
from . import views

urlpatterns = [
    path('', views.CandidatoListView, name='trabalhe_conoscos'),
    path('sucessos/', views.SucessosView, name='sucessos'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.BASE, name='BASE'),
    path('bestellingen/', views.bestellingen, name='bestellingen'),
    path('klanten/', views.klanten, name='klanten'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BASE, name='BASE'),
    path('bestellingen/', views.bestellingen, name='bestellingen'),
    path('klanten/', views.klanten, name='klanten'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-product/', views.create_product, name='create_product'),
    path('create-bestelling/', views.create_bestelling, name='create_bestelling'),
    path('bestelling-aanmaken/', views.bestelling_create_manual, name='bestelling_create_manual'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BASE, name='BASE'),
    path('bestellingen/', views.bestellingen, name='bestellingen'),
    path('bestellingen/<int:id>/', views.bestelling_detail, name='bestelling_detail'),
    path('bestellingen/bewerk/<int:id>/', views.bestelling_bewerk, name='bestelling_bewerk'),
    path('bestellingen/verwijder/<int:id>/', views.bestelling_verwijder, name='bestelling_verwijder'),
    path('bestellingen/mail/<int:id>/', views.bestelling_mail, name='bestelling_mail'),
    path('klanten/', views.klanten, name='klanten'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
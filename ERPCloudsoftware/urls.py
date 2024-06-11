from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from AdminInterface import views

urlpatterns = [
    # Views van de AdminInterface
    path('admin/', views.dashboard, name='admin_dashboard'),  
    path('bestellingen/', views.bestellingen, name='bestellingen'),
    path('klanten/', views.klanten, name='klanten'),
    path('bestellingen/<int:pk>/', views.bestelling_detail, name='bestelling_detail'),
    path('bestellingen/<int:pk>/bewerk/', views.bestelling_bewerk, name='bestelling_bewerk'),
    path('bestellingen/<int:pk>/verwijder/', views.bestelling_verwijder, name='bestelling_verwijder'),
    path('bestellingen/<int:pk>/mail/', views.bestelling_mail, name='bestelling_mail'),
    path('create-product/', views.create_product, name='create_product'),
    path('bestelling-aanmaken/', views.bestelling_create_manual, name='bestelling_create_manual'),
    path('producten/', views.product_list, name='product_list'),
    path('product-autocomplete/', views.product_autocomplete, name='product_autocomplete'),  # Zorg ervoor dat deze regel bestaat

    # Voeg hier de nieuwe URL-patronen toe
    path('simple-test/', views.simple_test_view, name='simple_test_view'),
    path('simple-test-success/', views.simple_test_success, name='simple_test_success'),

    # Anders
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('accounts/', include('allauth.urls')),  # Google Authentication Login
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
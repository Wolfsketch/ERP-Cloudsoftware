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

    # Anders
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('accounts/', include('allauth.urls')),  # Google Authentication Login

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
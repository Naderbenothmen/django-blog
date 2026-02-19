"""
URL configuration for proments project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from monitoring.views import home
from monitoring import views 
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('monitoring.urls')), 
     path('login/', views.login_view, name="login"),
     path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('', include('monitoring.urls')),
    path('', include('django.contrib.auth.urls')),
    
path('historique/', views.historique_view, name='historique'),
path('rapport/', views.rapport_view, name='rapport'),
path('logout/', LogoutView.as_view(next_page='login'), name='logout'),



] 


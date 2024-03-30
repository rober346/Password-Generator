"""
URL configuration for django_password_generator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from generator import views

urlpatterns = [
    # Se comenta para que no vaya al login de admin:
    # path('admin/', admin.site.urls),
    path('about', views.about, name='about'), # desde view se importa el about
    path('', views.home, name='home'), # desde view se importa el home
    path('generate-password', views.password, name='password'), # es posible poner "loquesea" en 'generate-password e igual funciona

]

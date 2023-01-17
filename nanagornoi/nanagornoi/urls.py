"""nanagornoi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_page.urls')),  # Домашняя страница
    path('steering_racks/', include('steering_racks.urls')),  # Страница ремонт рулевых реек
    path('turning_services/', include('turning_services.urls')),  # Страница токарных услуг
    path('other/', include('other.urls')),  # Страница прочие услуги
    path('location/', include('location.urls')),  # Страница с описанием местонахождения
    path('contacts/', include('contacts.urls')),  # Страница контакты
    path('blog/', include('blog.urls')),
    path('about/', include('about.urls'))  # Страница 'О нас'

]

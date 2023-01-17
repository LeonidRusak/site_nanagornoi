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
    path('', 'home_page.urls', {}),  # Домашняя страница
    path('steering_racks/', views.steering_racks_page),  # Страница ремонт рулевых реек
    path('turning_services/', views.turning_services_page),  # Страница токарных услуг
    path('other/', views.other_page),  # Страница прочие услуги
    path('location/', views.location_page),  # Страница с описанием местонахождения
    path('contacts/', views.contacts_page),  # Страница контакты
    path('about/', views.about_page)  # Страница 'О нас'

]

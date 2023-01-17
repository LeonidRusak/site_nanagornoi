from django.urls import path
from . import views


urlpatterns = [
    path('', views.turning_services_page)
]

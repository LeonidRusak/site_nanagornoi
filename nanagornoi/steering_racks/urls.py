from django.urls import path
from . import views


urlpatterns = [
    path('', views.steering_racks_page)
]

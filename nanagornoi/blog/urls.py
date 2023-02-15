from django.urls import path
from . import views


# URL адреса в приложении блог
urlpatterns = [
    path('', views.blog_page, name='blog_page'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('<category>/', views.blog_category, name='blog_category')
]

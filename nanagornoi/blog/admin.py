from django.contrib import admin
from .models import Post, Category

# Модели (таблицы БД) зарегистрированные в административной панели
admin.site.register(Post)
admin.site.register(Category)

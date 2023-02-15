from django.db import models


class Category(models.Model):
    # Категория поста в блоге
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    # Модель поста в блоге, в административной панели при создании самого поста, можно выбирать несколько категорий
    title = models.CharField(max_length=250)
    post_img = models.ImageField(upload_to='static/post_img/', null=True, blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return self.title

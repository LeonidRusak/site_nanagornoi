# Generated by Django 4.1.5 on 2023-02-13 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_post_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_img',
        ),
    ]

# Generated by Django 4.1.5 on 2023-02-13 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(height_field=100, upload_to='post_img/', width_field=100),
        ),
    ]

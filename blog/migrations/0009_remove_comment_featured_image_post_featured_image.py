# Generated by Django 4.2.11 on 2024-03-18 17:28

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='featured_image',
        ),
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]

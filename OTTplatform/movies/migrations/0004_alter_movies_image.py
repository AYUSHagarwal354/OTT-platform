# Generated by Django 4.2.7 on 2024-03-07 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movies_description_movies_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='image',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]

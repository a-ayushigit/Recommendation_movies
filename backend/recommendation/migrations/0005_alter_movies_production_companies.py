# Generated by Django 5.0.6 on 2024-06-27 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0004_remove_movies_genres_delete_genre_movies_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='production_companies',
            field=models.CharField(max_length=1000),
        ),
    ]

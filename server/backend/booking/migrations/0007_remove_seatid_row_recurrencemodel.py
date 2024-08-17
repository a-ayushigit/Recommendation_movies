# Generated by Django 5.0.7 on 2024-08-17 05:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_remove_seatid_type_seatid_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seatid',
            name='row',
        ),
        migrations.CreateModel(
            name='RecurrenceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('recurrence_type', models.CharField(choices=[('daily', 'daily'), ('weekly', 'weekly'), ('monthly', 'monthly')], default='daily', max_length=7)),
                ('interval', models.IntegerField(default=1)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('theatre_movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.theatremovie')),
            ],
        ),
    ]

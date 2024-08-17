# Generated by Django 5.0.7 on 2024-07-30 06:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_seat_seat_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seatid',
            name='type',
        ),
        migrations.AddField(
            model_name='seatid',
            name='type',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='booking.seattype'),
        ),
    ]

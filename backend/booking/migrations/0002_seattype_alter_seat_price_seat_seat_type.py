# Generated by Django 5.0.6 on 2024-07-09 10:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeatType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='seat',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AddField(
            model_name='seat',
            name='seat_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.seattype'),
        ),
    ]

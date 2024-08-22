# Generated by Django 5.0.7 on 2024-08-22 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_remove_seatid_row_recurrencemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat_arrangement',
            name='no_cols',
        ),
        migrations.RemoveField(
            model_name='seat_arrangement',
            name='no_rows',
        ),
        migrations.AlterField(
            model_name='show',
            name='id',
            field=models.AutoField(db_index=True, primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 5.0 on 2023-12-18 07:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_alter_daily_atendance_check_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_atendance',
            name='check_in',
            field=models.TimeField(default=datetime.time(13, 1, 28, 677228)),
        ),
    ]

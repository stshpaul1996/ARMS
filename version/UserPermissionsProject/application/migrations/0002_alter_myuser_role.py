# Generated by Django 4.2.7 on 2024-02-09 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='application.role'),
        ),
    ]

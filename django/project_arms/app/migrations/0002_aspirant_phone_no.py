# Generated by Django 4.2.7 on 2023-12-12 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aspirant',
            name='phone_no',
            field=models.CharField(max_length=13, null=True, verbose_name='Phone Number'),
        ),
    ]

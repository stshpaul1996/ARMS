# Generated by Django 4.2.7 on 2024-03-15 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.IntegerField()),
                ('maths', models.IntegerField()),
                ('science', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 4.2.6 on 2023-12-19 03:13

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cricketers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("image_path", models.CharField(max_length=250)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 4.2.6 on 2024-02-04 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Trip",
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
                ("created_by", models.CharField(default=None, max_length=250)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_by", models.CharField(default=None, max_length=250)),
                ("updated_at", models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name="Member",
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
                ("created_by", models.CharField(default=None, max_length=250)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_by", models.CharField(default=None, max_length=250)),
                ("updated_at", models.DateTimeField(default=None)),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="TripApp.trip"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Expenses",
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
                ("spent", models.IntegerField()),
                ("spent_for", models.TextField()),
                ("created_by", models.CharField(default=None, max_length=250)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_by", models.CharField(default=None, max_length=250)),
                ("updated_at", models.DateTimeField(default=None)),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="TripApp.member"
                    ),
                ),
            ],
        ),
    ]

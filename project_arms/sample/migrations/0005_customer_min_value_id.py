# Generated by Django 4.2.6 on 2023-12-08 01:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sample", "0004_customer_value_less_zero"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="min_value_id",
            field=models.SmallIntegerField(
                default=23,
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=23, message="value should greater than zero"
                    )
                ],
            ),
        ),
    ]

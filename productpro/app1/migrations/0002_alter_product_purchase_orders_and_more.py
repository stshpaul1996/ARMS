# Generated by Django 4.2.6 on 2024-01-05 14:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="purchase_orders",
            field=models.ManyToManyField(blank=True, to="app1.purchaseorder"),
        ),
        migrations.AlterField(
            model_name="product",
            name="sales_orders",
            field=models.ManyToManyField(blank=True, to="app1.salesorder"),
        ),
    ]

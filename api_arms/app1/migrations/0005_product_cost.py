# Generated by Django 4.0 on 2024-01-04 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_category_purchaseorder_salesorder_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

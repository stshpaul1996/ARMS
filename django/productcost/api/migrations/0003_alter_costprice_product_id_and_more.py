# Generated by Django 4.2.7 on 2024-01-06 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_product_unque_number_product_product_unique_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costprice',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_costs', to='api.product'),
        ),
        migrations.AlterField(
            model_name='openingstock',
            name='prodcut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock', to='api.product'),
        ),
    ]

# Generated by Django 4.2.7 on 2024-01-06 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('product_unque_number', models.CharField(max_length=250, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.category')),
                ('purchase_orders', models.ManyToManyField(to='api.purchaseorder')),
                ('sales_orders', models.ManyToManyField(to='api.salesorder')),
            ],
        ),
        migrations.CreateModel(
            name='OpeningStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prodcut', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.product')),
            ],
        ),
        migrations.CreateModel(
            name='CostPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.product')),
            ],
        ),
    ]

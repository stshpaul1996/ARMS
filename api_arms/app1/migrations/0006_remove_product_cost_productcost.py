# Generated by Django 4.0 on 2024-01-05 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_product_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cost',
        ),
        migrations.CreateModel(
            name='ProductCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('prodcut', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app1.product')),
            ],
        ),
    ]

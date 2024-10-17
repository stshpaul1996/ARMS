# Generated by Django 5.0.6 on 2024-06-04 07:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HazardousMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('un_number', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('placard_image_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='TransportRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('mixed_quantity', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.hazardousmaterial')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_at', models.DateTimeField(auto_now_add=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transport_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.transportrecord')),
            ],
        ),
    ]

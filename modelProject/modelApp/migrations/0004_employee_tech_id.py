# Generated by Django 4.2.7 on 2023-12-08 06:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("modelApp", "0003_alter_employee_email_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="tech_id",
            field=models.IntegerField(default=656),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0 on 2023-12-28 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_alter_aspirant_experience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aspirant',
            name='Do_you_Have_PF_in_last_company',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=100, null=True),
        ),
    ]

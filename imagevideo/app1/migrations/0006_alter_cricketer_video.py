# Generated by Django 4.2.4 on 2023-12-21 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_cricketer_image_path_alter_cricketer_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cricketer',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/', verbose_name='Video'),
        ),
    ]

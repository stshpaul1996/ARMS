# Generated by Django 5.0 on 2023-12-28 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aspirant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('F_name', models.CharField(max_length=100, null=True, verbose_name='First name')),
                ('L_name', models.CharField(max_length=100, null=True, verbose_name='Last name')),
                ('Email_id', models.EmailField(max_length=100, null=True)),
                ('Phone_no', models.IntegerField(help_text='Enter your phone number', null=True)),
                ('Graduation', models.CharField(choices=[('btech', 'B.Tech'), ('bsc', 'B.Sc'), ('ba', 'B.A'), ('bcom', 'B.Com'), ('degree', 'Degree')], max_length=10, null=True)),
                ('Graduation_Stream', models.CharField(max_length=100, null=True)),
                ('Graduation_Passed_Out_Year', models.IntegerField(help_text='passed out year should be >2016 and <2023', null=True)),
                ('Post_Graduation', models.CharField(choices=[('mtech', 'M.Tech'), ('mba', 'MBA'), ('mca', 'MCA'), ('mcom', 'M.COM'), ('msc', 'M.SC')], max_length=10)),
                ('Post_Graduation_Stream', models.CharField(max_length=100)),
                ('Post_Gradation_Passed_out_year', models.IntegerField(help_text='passed out year should be >2016 and <2023', null=True)),
                ('Trained_on_Technology', models.CharField(choices=[('python', 'Python'), ('java', 'JAVA'), ('.net', '.NET'), ('reactjs', 'ReactJS'), ('salesforce', 'Salesforce'), ('devops', 'Devops')], max_length=10, null=True)),
                ('Where_did_you_trained_Institute_Name', models.CharField(max_length=100, null=True)),
                ('Duration_of_Course', models.CharField(max_length=100, null=True)),
                ('Reference_Name', models.CharField(max_length=50)),
                ('Where_did_you_hear_about_the_interview', models.CharField(max_length=100, null=True)),
                ('Experience', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
                ('Previous_Company_Name', models.CharField(max_length=50, null=True)),
                ('Current_CTC', models.BigIntegerField(null=True)),
                ('Expected_CTC', models.BigIntegerField(null=True)),
                ('Do_you_Have_PF_in_last_company', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=100, null=True)),
                ('How_Many_years_of_Experience', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

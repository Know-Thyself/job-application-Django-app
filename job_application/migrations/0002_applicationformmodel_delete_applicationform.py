# Generated by Django 4.2.4 on 2023-08-24 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationFormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField(verbose_name='start date')),
                ('occupation', models.CharField(max_length=80)),
            ],
        ),
        migrations.DeleteModel(
            name='ApplicationForm',
        ),
    ]

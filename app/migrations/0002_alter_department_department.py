# Generated by Django 4.0.4 on 2022-05-18 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department',
            field=models.CharField(max_length=40),
        ),
    ]
# Generated by Django 3.2.16 on 2023-01-21 22:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(max_length=64, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
    ]

# Generated by Django 3.2.16 on 2023-01-23 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

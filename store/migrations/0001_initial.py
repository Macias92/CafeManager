# Generated by Django 3.2.16 on 2023-01-21 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0002_alter_supplier_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('sku_number', models.CharField(max_length=64)),
                ('quantity', models.IntegerField(default=0)),
                ('unit', models.PositiveSmallIntegerField(choices=[(1, 'ml'), (2, 'g')], default=1)),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='supplier.supplier')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]

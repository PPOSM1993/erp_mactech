# Generated by Django 5.0.4 on 2024-04-18 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0062_salecotizacion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SaleCotizacion',
            new_name='Sale',
        ),
    ]
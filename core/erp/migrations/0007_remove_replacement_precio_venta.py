# Generated by Django 5.0.3 on 2024-03-25 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0006_replacement_code_replacement"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="replacement",
            name="precio_venta",
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-04 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0056_rename_cant_detcotizacion_stock"),
    ]

    operations = [
        migrations.RenameField(
            model_name="detcotizacion",
            old_name="stock",
            new_name="cant",
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-28 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0032_remove_replacement_precio_compra"),
    ]

    operations = [
        migrations.AlterField(
            model_name="replacement",
            name="stock",
            field=models.CharField(default=0, verbose_name="Stock"),
        ),
    ]

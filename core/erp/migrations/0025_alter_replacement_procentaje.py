# Generated by Django 5.0.3 on 2024-03-27 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0024_replacement_procentaje"),
    ]

    operations = [
        migrations.AlterField(
            model_name="replacement",
            name="procentaje",
            field=models.DecimalField(
                decimal_places=2, default=1.4, max_digits=9, verbose_name="Porcentaje"
            ),
        ),
    ]

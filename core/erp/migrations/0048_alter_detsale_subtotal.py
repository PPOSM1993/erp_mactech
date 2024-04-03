# Generated by Django 5.0.3 on 2024-04-02 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0047_alter_detsale_subtotal"),
    ]

    operations = [
        migrations.AlterField(
            model_name="detsale",
            name="subtotal",
            field=models.DecimalField(
                decimal_places=2, default=0.0, max_digits=9, verbose_name="Subtotal"
            ),
        ),
    ]
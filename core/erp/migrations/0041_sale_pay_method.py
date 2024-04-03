# Generated by Django 5.0.3 on 2024-04-01 17:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0040_paymethods"),
    ]

    operations = [
        migrations.AddField(
            model_name="sale",
            name="pay_method",
            field=models.ForeignKey(
                default=40,
                on_delete=django.db.models.deletion.PROTECT,
                to="erp.paymethods",
                verbose_name="Método de Pago",
            ),
            preserve_default=False,
        ),
    ]

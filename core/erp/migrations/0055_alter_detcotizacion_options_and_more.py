# Generated by Django 5.0.3 on 2024-04-03 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0054_alter_replacement_cant_detcotizacion"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="detcotizacion",
            options={
                "ordering": ["id"],
                "verbose_name": "Detalle Cotización",
                "verbose_name_plural": "Detalle Cotizaciones",
            },
        ),
        migrations.RenameField(
            model_name="detcotizacion",
            old_name="prod",
            new_name="repl",
        ),
        migrations.AddField(
            model_name="cotizacion",
            name="money",
            field=models.ForeignKey(
                default=54,
                on_delete=django.db.models.deletion.PROTECT,
                to="erp.money",
                verbose_name="Moneda",
            ),
            preserve_default=False,
        ),
    ]

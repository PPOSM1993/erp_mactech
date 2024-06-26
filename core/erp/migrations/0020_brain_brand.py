# Generated by Django 5.0.3 on 2024-03-26 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0019_rename_customer_clients"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brain",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=150, unique=True, verbose_name="Nombre Marca"
                    ),
                ),
            ],
            options={
                "verbose_name": "Marca",
                "verbose_name_plural": "Marcas",
                "ordering": ["id"],
            },
        ),
    ]

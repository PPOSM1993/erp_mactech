# Generated by Django 5.0.3 on 2024-03-26 15:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0012_category_date_creation_category_date_updated_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
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
                    "names",
                    models.CharField(
                        max_length=150, unique=True, verbose_name="Empresa"
                    ),
                ),
                (
                    "dni",
                    models.CharField(
                        max_length=12,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Formato de Rut Incorrecto.",
                                regex="^0*(\\d{1,3}(\\.?\\d{3})*)\\-?([\\dkK])$",
                            )
                        ],
                        verbose_name="RUT",
                    ),
                ),
                (
                    "commercial_business",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        null=True,
                        verbose_name="Giro Comercial",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        max_length=17,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="El número de telefono debe tener el siguiente formato: '+999999999'.",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                        verbose_name="Telefono",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="Dirección"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="Ciudad"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=150,
                        null=True,
                        unique=True,
                        verbose_name="Email",
                    ),
                ),
            ],
            options={
                "verbose_name": "Cliente",
                "verbose_name_plural": "Clientes",
                "ordering": ["id"],
            },
        ),
    ]

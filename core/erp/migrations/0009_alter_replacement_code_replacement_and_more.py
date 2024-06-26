# Generated by Django 5.0.3 on 2024-03-25 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0008_replacement_cat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="replacement",
            name="code_replacement",
            field=models.CharField(
                max_length=150, null=True, unique=True, verbose_name="Código"
            ),
        ),
        migrations.AlterField(
            model_name="replacement",
            name="name",
            field=models.CharField(
                max_length=150, null=True, unique=True, verbose_name="Nombre"
            ),
        ),
    ]

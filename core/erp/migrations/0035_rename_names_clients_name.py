# Generated by Django 5.0.3 on 2024-04-01 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("erp", "0034_rename_name_clients_names"),
    ]

    operations = [
        migrations.RenameField(
            model_name="clients",
            old_name="names",
            new_name="name",
        ),
    ]

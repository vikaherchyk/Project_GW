# Generated by Django 4.2.13 on 2024-05-22 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("goods", "0009_alter_products_quantity"),
    ]

    operations = [
        migrations.CreateModel(
            name="Booked",
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
                    models.CharField(max_length=150, unique=True, verbose_name="Назва"),
                ),
            ],
        ),
    ]

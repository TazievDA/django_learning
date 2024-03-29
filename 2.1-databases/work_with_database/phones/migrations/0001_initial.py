# Generated by Django 5.0.3 on 2024-03-20 08:04

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Phone",
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
                ("name", models.CharField(verbose_name=25)),
                ("price", models.IntegerField()),
                ("image", models.CharField(verbose_name=255)),
                ("release_date", models.DateTimeField()),
                ("lte_exists", models.BooleanField()),
                ("slug", models.SlugField()),
            ],
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-20 09:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("phones", "0002_alter_phone_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="phone",
            name="slug",
            field=models.SlugField(max_length=255),
        ),
    ]
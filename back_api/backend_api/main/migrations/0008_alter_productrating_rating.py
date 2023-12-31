# Generated by Django 4.2.7 on 2023-11-24 03:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_alter_productrating_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productrating",
            name="rating",
            field=models.PositiveSmallIntegerField(
                validators=[
                    django.core.validators.MinValueValidator,
                    django.core.validators.MaxValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ]
            ),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-23 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_rename_reviews_productrating_reviews"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productrating",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_ratings",
                to="main.product",
            ),
        ),
    ]

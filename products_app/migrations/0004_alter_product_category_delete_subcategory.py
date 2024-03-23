# Generated by Django 5.0.3 on 2024-03-23 06:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0003_category_product_product_id_subcategory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products_app.category'),
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-30 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0003_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
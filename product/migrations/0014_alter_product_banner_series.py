# Generated by Django 3.2.24 on 2024-03-17 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_remove_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_banner',
            name='series',
            field=models.TextField(max_length=30, null=True),
        ),
    ]

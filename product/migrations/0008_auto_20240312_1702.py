# Generated by Django 3.2.25 on 2024-03-12 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discounted',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='new',
            field=models.BooleanField(default=None, null=True),
        ),
    ]

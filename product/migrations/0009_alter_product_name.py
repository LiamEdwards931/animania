# Generated by Django 3.2.25 on 2024-03-12 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20240312_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.TextField(max_length=40, unique=True),
        ),
    ]

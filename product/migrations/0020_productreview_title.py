# Generated by Django 3.2.24 on 2024-03-20 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_productreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
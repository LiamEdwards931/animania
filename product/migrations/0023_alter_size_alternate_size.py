# Generated by Django 3.2.24 on 2024-04-01 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_alter_size_size_quantity_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='alternate_size',
            field=models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default=None, max_length=10, null=True),
        ),
    ]

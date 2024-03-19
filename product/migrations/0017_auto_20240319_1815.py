# Generated by Django 3.2.24 on 2024-03-19 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_auto_20240319_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sizes',
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=2, null=True),
        ),
        migrations.DeleteModel(
            name='ProductSize',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]

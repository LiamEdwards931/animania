# Generated by Django 3.2.24 on 2024-03-08 16:03

import cloudinary.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
                ('alternative_images', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
                ('name', models.TextField(max_length=40)),
                ('description', models.TextField()),
                ('series', models.TextField(max_length=30)),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('slug', models.SlugField(unique=True)),
                ('category', models.CharField(max_length=50)),
                ('sub_category', models.CharField(max_length=50)),
                ('search_tags', models.CharField(blank=True, max_length=100)),
                ('quantity_available', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('new', models.BooleanField(default=False)),
                ('discounted', models.BooleanField(default=False)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('related_products', models.ManyToManyField(blank=True, related_name='_product_product_related_products_+', to='product.Product')),
            ],
        ),
    ]
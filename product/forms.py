from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'series', 'price',
                  'slug', 'category', 'sub_category', 'search_tags',
                  'related_products',
                  'quantity_available', 'new', 'discounted', 'size']
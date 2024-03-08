from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity_available', 'new', 'discounted', 'created_on', 'updated_on','size')
    list_filter = ('category', 'sub_category', 'new', 'discounted', 'created_on', 'updated_on')
    search_fields = ('name', 'description', 'series', 'category', 'sub_category', 'search_tags')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_on', 'updated_on')

admin.site.register(Product, ProductAdmin)
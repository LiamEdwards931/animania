from django.contrib import admin
from .models import Product, product_banner,ProductReview,Size, Wishlist

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity_available', 'new', 'discounted', 'created_on', 'updated_on')
    list_filter = ('category', 'sub_category', 'new', 'discounted', 'created_on', 'updated_on')
    search_fields = ('name', 'description', 'series', 'category', 'sub_category', 'search_tags')
    readonly_fields = ('created_on', 'updated_on')

admin.site.register(Product, ProductAdmin)

admin.site.register(product_banner)

admin.site.register(ProductReview)

admin.site.register(Size)

admin.site.register(Wishlist)
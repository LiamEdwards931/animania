from product.models import Product

def products_context(request):
    products = Product.objects.all()
    series_list = sorted(Product.objects.values_list('series', flat=True).distinct())
    category_list = sorted(Product.objects.values_list('category', flat=True).distinct())
    
    context={
        'products': products,
        'series': series_list,
        'categories': category_list,
    }
    
    return context


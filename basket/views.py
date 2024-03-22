from django.shortcuts import render
from product.models import Product

# Create your views here.

def basket(request):
    products = Product.objects.all()
    product_count = products.count()
    

    context = {
        'products': products,
        'product_count': product_count
    }
    
    return render(request,'basket.html', context)
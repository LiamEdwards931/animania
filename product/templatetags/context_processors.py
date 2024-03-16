from product.models import Product
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q

def products_context(request):
    products = Product.objects.all()  # Retrieve all products
    return {'products': products}  # Return the products in a dictionary

def product_search_context(request):
    """
    Context processor for product search functionality
    """
    context = {}
    query = request.GET.get('q', '')
    next_url = request.GET.get('next', '/')

    if query:
        products = Product.objects.filter(
            Q(search_tags__icontains=query) | Q(description__icontains=query)
        )
        context['products'] = products
        context['search_term'] = query
        context['show_shop_all'] = True
    else:
        messages.error(request, 'No products found.')
        context['redirect_url'] = next_url

    return context

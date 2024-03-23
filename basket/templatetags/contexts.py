from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404
from product.models import Product

def basket_context(request):

    basket_products = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})
    subtotal = 0


    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        if product.discounted:
            total += quantity * product.discounted_price
            subtotal = quantity * product.discounted_price
        else:
            total += quantity * product.price
            subtotal = quantity * product.price
        
        product_count += quantity
        basket_products.append({
            'product_id': item_id,
            'quantity': quantity,
            'product': product,
            'subtotal': subtotal,
        })

    if total < settings.DELIVERY_AMOUNT:
        delivery = total * Decimal(settings.DELIVERY_COST/ 100)
        free_delivery_delta = settings.DELIVERY_AMOUNT - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context ={
        'basket_products': basket_products,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery': settings.DELIVERY_AMOUNT,
        'grand_total': grand_total,
        'product': Product,
    }

    return context
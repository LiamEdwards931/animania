from decimal import Decimal
from django.conf import settings
from product.models import Product
from django.shortcuts import get_object_or_404

def basket_context(request):

    bag_items = []
    total = 0
    product_count = 0
    basket = request.session.get('bag', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        if product.discounted:
            total += quantity * product.discounted_price
            subtotal = quantity * product.discounted_price
        else:
            total += quantity * product.price
            subtotal = quantity * product.price
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product':product,
            'subtotal': subtotal,
        })
        
        if total < settings.DELIVERY_AMOUNT:
            delivery = total * Decimal(settings.DELIVERY_COST / 100)
            free_delivery_delta = settings.DELIVERY_AMOUNT - total
        else:
            delivery = 0
            free_delivery_delta = 0
        
        grand_total = delivery + total
        
        context = {
            'bag_items': bag_items,
            'total': total,
            'product_count': product_count,
            'delivery': delivery,
            'free_delivery_delta': free_delivery_delta,
            'free_delivery_threshold': settings.DELIVERY_AMOUNT,
            'grand_total': grand_total,
        }

    return context
from django.conf import settings
from decimal import Decimal

def basket_context(request):

    basket_products = []
    total = 0
    product_count = 0

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
    }

    return context
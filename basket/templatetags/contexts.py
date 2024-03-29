from decimal import Decimal
from django.conf import settings
from product.models import Product,Size
from django.shortcuts import get_object_or_404
from django.contrib import messages

def basket_context(request):
    bag_items = []
    total = 0
    product_count = 0
    basket = request.session.get('bag', {})

    for item_id, item_data in basket.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            if product.discounted:
                total += item_data * product.discounted_price
                subtotal = item_data * product.discounted_price
            else:
                total += item_data * product.price
                subtotal = item_data * product.price
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'subtotal': subtotal,
            })
        else:
            for size, quantity in item_data['products_by_size'].items():
                product = get_object_or_404(Product, pk=item_id)
                size_instance = get_object_or_404(Size, alternate_size=size, product=product)
                print(f"Type of size_instance: {type(size_instance)}")
                if product.discounted:
                    total += quantity * product.discounted_price
                    subtotal = quantity * product.discounted_price
                else:
                    total += quantity * product.price
                    subtotal = quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'subtotal': subtotal,
                    'size': size_instance,
                })
                print(bag_items)
 
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

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from . import forms
from .forms import OrderForm
from accounts.models import Address
from product.models import Product, Size
from .models import OrderLine, Order
from basket.templatetags.contexts import basket_context
import stripe
from django.conf import settings
from django.db import transaction

# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line = OrderLine(
                           order=order,
                           product=product,
                           quantity=item_data
                        )
                        order_line.save()
                    else:
                        products_by_size = item_data['products_by_size']
                        for size, quantity in products_by_size.items():
                            size_instances = (
                                    Size.objects.filter(product=product,
                                                        alternate_size=size)
                                )
                            for size_instance in size_instances:
                                order_line = OrderLine(
                                    order=order,
                                    product=product,
                                    quantity=quantity,
                                    product_size=size_instance,
                                )
                                order_line.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        'The item you are trying to purchase was'
                        'not found in our database,'
                        'please contact us'
                        ))
                    order.delete()
                    return redirect(reverse('basket'))
            return redirect(reverse(
                 'checkoutSuccess', args=[order.order_number]))
        else:
            messages.error(request,
                           'There was an issue with your form,'
                           'please double check all the'
                           'information is correct.')

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, 'Your basket is empty')
            return redirect(reverse('allproducts'))

    current_basket = basket_context(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY
    )
    print(intent)

    if request.user.is_authenticated:
        user = request.user
        addresses = Address.objects.filter(user=user)
        if addresses.exists():
            address = addresses.first()
            initial_data = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'door_number': address.door_number,
                'street': address.street,
                'city': address.city,
                'county': address.state,
                'country': address.country,
                'postal_code': address.postal_code,
            }
        else:
            initial_data = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
            }
        order_form = forms.OrderForm(initial_data)
    else:
        order_form = forms.OrderForm()

    if not stripe_public_key:
        messages.warning('Did you forget your Stripe Public Key?')

    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    View that will display on a successful checkout
    """
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request,
                     f"Your order has been completed,"
                     f"your order number is: {order_number}")
    if 'bag' in request.session:
        del request.session['bag']

    update_product_quantities(order)

    template = 'checkout_success.html'

    context = {
        'order': order,
    }

    return render(request, template, context)


@transaction.atomic
def update_product_quantities(order):
    for line_item in order.lineitems.all():
        product = line_item.product
        quantity_purchased = line_item.quantity

        if line_item.product_size:
            size = line_item.product_size
            size.size_quantity_available -= quantity_purchased
            size.save()
        else:
            product.quantity_available -= quantity_purchased
            product.save()

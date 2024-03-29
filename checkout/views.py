from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from . import forms
from accounts.models import Address
from basket.templatetags.contexts import basket_context
import stripe
from django.conf import settings

# Create your views here.

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    bag = request.session.get('bag',{})
    if not bag:
        messages.error(request,'Your basket is empty')
        return redirect(reverse('allproducts'))
    template = 'checkout.html'
    
    
    current_basket = basket_context(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount = stripe_total,
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
                'street' : address.street,
                'city' : address.city,
                'county' : address.state,
                'country' :address.country,
                'postal_code' : address.postal_code,
            }
        order_form = forms.OrderForm(initial_data)
    else:
        order_form = forms.OrderForm()

    if not stripe_public_key:
        messages.warning('Did you forget your Stripe Public Key?')
    
    context ={
        'order_form':order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    
    return render(request, template, context)
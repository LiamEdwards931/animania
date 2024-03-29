from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from . import forms
from accounts.models import Address

# Create your views here.

def checkout(request):
    bag = request.session.get('bag',{})
    if not bag:
        messages.error(request,'Your basket is empty')
        return redirect(reverse('allproducts'))
    template = 'checkout.html'
    
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

    context ={
        'order_form':order_form,
        'stripe_public_key':'pk_test_51OzJZPGiFvkcenzZK9VSVu9XPPPUzX98it6nibktnVsnQkq4MvTP6jBY8jZdmVbstNHVaLeC9Mr4tTIX15zuASAN00Vk3v73YO',
        'client_secret': 'test_secret',
    }
    
    return render(request, template, context)
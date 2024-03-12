from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Product
from . import forms

# Create your views here.

def index(request):
    messages_to_render = messages.get_messages(request)
    return render(request, 'index.html',{'messages': messages_to_render})

def amendProducts(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }
        
    return render(request, 'amendproducts.html', context )

def newProduct(request):
    if request.method == 'POST':
        # If the form has been submitted, process the data
        newProductForm = forms.ProductForm(request.POST, request.FILES)
        if newProductForm.is_valid():
            newProductForm.save()
            messages.success(request, "Your Product has been added successfully")
            return redirect('amendProducts') 
    else:
        newProductForm = forms.ProductForm()
    
    return render(request, 'new_product.html', {'form': newProductForm})
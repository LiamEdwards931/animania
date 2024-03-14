from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Product
from . import forms
from .forms import ProductForm

# Create your views here.

def index(request):
    """
     Creates a view to render index.html, 
     renders all product and message instances
    """
    messages_to_render = messages.get_messages(request)
    products = Product.objects.all()

    context = {
        'products': products,
        'messages': messages_to_render,
    }
    
    return render(request, 'index.html', context)


def amendProducts(request):
    """
    Renders the amend Products.html page, 
    Gets all product instances.
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }
        
    return render(request, 'amendproducts.html', context )

def newProduct(request):
    """
    Renders the product form for adding a new product,
    renders new_product.html
    """
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

@user_passes_test(lambda u: u.is_superuser)
def delete_product(request, product_id):
    """
    View to delete a product instance on request by a superuser.
    """
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        # Delete the product
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('amendProducts')
    else:
        # If the request method is not POST, display the following error
        messages.error(request, 'Could not delete product. Invalid request method.')
        return redirect('amendProducts')
    
@user_passes_test(lambda u: u.is_superuser)
def update_product(request, product_id):
    """
    View to Edit a product instance on request by a superuser.
    """
    # Get the existing product instance
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        # Populate the form with the new POST data and the existing product data
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully')
            return redirect('amendProducts')
    else:
        # Populate the form with the existing product data only
        form = ProductForm(instance=product)
    
    context = {
        'form': form,
        'product_id': product_id,
    }
    return render(request, 'update_product.html', context)
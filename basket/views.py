from django.shortcuts import render, redirect
from product.models import Product

# Create your views here.

def basket(request):
    """
    View for displaying the basket html file.
    """
    products = Product.objects.all()
    product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    
    return render(request,'basket.html', context)

def add_to_basket(request,product_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('selected_size')
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)

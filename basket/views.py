from django.shortcuts import render, redirect, reverse, HttpResponse
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

def add_to_basket(request,item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'selected_size' in request.POST:
        size = request.POST['selected_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['products_by_size'].keys():
                bag[item_id]['products_by_size'][size] += quantity
            else:
                bag[item_id]['products_by_size'][size] = quantity
        else:
            bag[item_id] = {'products_by_size': {size: quantity}}
    else:
    
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'selected_size' in request.POST:
        size = request.POST['selected_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['products_by_size'][size] = quantity
        else:
            del bag[item_id]['products_by_size'][size]
            if not bag[item_id]['products_by_size']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('basket'))

def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        size = None
        if 'selected_size' in request.POST:
            size = request.POST['selected_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['products_by_size'][size]
            if not bag[item_id]['products_by_size']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except KeyError:
        return HttpResponse(status=400)
    except Exception:
        return HttpResponse(status=500)
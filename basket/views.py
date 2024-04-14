from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
    )
from product.models import Product, Size
from django.contrib import messages


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

    return render(request, 'basket.html', context)


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'selected_size' in request.POST:
        size = request.POST['selected_size']

    if size:
        product = get_object_or_404(Product, id=item_id)
        size_exists = Size.objects.filter(
            product=product, alternate_size=size).exists()
        if not size_exists:
            messages.error(
                request, "The selected size does not exist for this product.")
            return redirect(redirect_url)

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

    product = get_object_or_404(Product, id=item_id)

    if size:
        size_object = get_object_or_404(
            Size, product=product, alternate_size=size)
        if quantity > size_object.size_quantity_available:
            messages.error(
                request,
                f"The selected quantity"
                f"exceeds the available quantity for size {size}.")
            return redirect(redirect_url)
    else:
        if quantity > product.quantity_available:
            messages.error(
                request, "The selected quantity"
                "exceeds the available quantity.")
            return redirect(redirect_url)

    request.session['bag'] = bag
    product_name = Product.objects.get(id=item_id).name
    if size:
        messages.success(
             request,
             f"{quantity} x {product_name}:"
             f"{ size } added to your basket.")
    else:
        messages.success(
            request,
            f"{quantity} x {product_name} added to your basket.")
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'selected_size' in request.POST:
        size = request.POST['selected_size']
    bag = request.session.get('bag', {})

    if item_id in bag:
        if size:  # If size is specified
            if quantity > 0:
                """
                Check if the product has
                'products_by_size' dictionary in the bag
                """
                if 'products_by_size' in bag[item_id]:
                    bag[item_id]['products_by_size'][size] = quantity
                else:
                    # Create 'products_by_size' dictionary if it doesn't exist
                    bag[item_id]['products_by_size'] = {size: quantity}
            else:
                # If quantity is 0 or less, remove the specified size
                if size in bag[item_id]['products_by_size']:
                    del bag[item_id]['products_by_size'][size]
                    if not bag[item_id]['products_by_size']:
                        # If there are no more sizes for the product,
                        # remove the product from the bag
                        bag.pop(item_id)
        else:  # If size is not specified
            if quantity > 0:
                # Update the quantity for the product
                bag[item_id] = quantity
            else:
                # If quantity is 0 or less, remove the product from the bag
                bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('basket'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        size = request.POST.get('selected_size')
        bag = request.session.get('bag', {})

        if size:
            if item_id in bag:
                if size in bag[item_id]['products_by_size']:
                    del bag[item_id]['products_by_size'][size]
                    if not bag[item_id]['products_by_size']:
                        bag.pop(item_id)
        elif item_id in bag:
            bag.pop(item_id)

        request.session['bag'] = bag
        product_name = Product.objects.get(id=item_id).name
        if size:
            messages.success(
                request,
                f"{product_name}: { size } removed from your basket.")
        else:
            messages.success(
                request,
                f"{product_name} removed from your basket.")
        return redirect(reverse('basket'))

    except KeyError:
        return HttpResponse(status=400)
    except Exception:
        return HttpResponse(status=500)

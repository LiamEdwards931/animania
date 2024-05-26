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
    # Get the quantity of the product already in the bag
    existing_quantity = get_quantity_in_bag(bag, item_id, size)

    """
    Calculate the total quantity (existing + selected)
    and check against available quantity
    """
    total_quantity = existing_quantity + quantity

    product = get_object_or_404(Product, id=item_id)

    if size:
        size_object = get_object_or_404(
            Size, product=product, alternate_size=size)
        if total_quantity > size_object.size_quantity_available:
            messages.error(
                request,
                (
                 f"The selected quantity exceeds the"
                 f"available quantity for size {size}."
                )
            )
            return redirect(redirect_url)
    else:
        if total_quantity > product.quantity_available:
            messages.error(
                request,
                (
                 "The selected quantity exceeds the available quantity."
                )
            )
            return redirect(redirect_url)

    # Update the bag with the new quantity
    if size:
        if item_id in bag:
            if size in bag[item_id]['products_by_size']:
                bag[item_id]['products_by_size'][size] += quantity
            else:
                bag[item_id]['products_by_size'][size] = quantity
        else:
            bag[item_id] = {'products_by_size': {size: quantity}}
    else:
        if item_id in bag:
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag

    product_name = Product.objects.get(id=item_id).name
    if size:
        messages.success(
            request,
            f"{quantity} x {product_name}: {size} added to your basket.")
    else:
        messages.success(
            request,
            f"{quantity} x {product_name} added to your basket.")

    return redirect(redirect_url)


def get_quantity_in_bag(bag, item_id, size=None):
    """
    Get the quantity of a specific product
    (optionally with a specified size) in the basket.
    """
    if item_id in bag:
        if size:
            return bag[item_id].get('products_by_size', {}).get(size, 0)
        else:
            return bag[item_id]
    else:
        return 0


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'selected_size' in request.POST:
        size = request.POST['selected_size']
    bag = request.session.get('bag', {})

    if item_id in bag:
        product = get_object_or_404(Product, id=item_id)
        if size:  # If size is specified
            size_object = get_object_or_404(
                    Size, product=product, alternate_size=size)
            if quantity > 0:
                """
                Check if the selected quantity exceeds
                the available quantity for the size
                """
                if quantity > size_object.size_quantity_available:
                    messages.error(
                        request,
                        f"The selected quantity exceeds"
                        f" the available quantity"
                        f"for size {size}.")
                    return redirect(reverse('basket'))

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
                """
                Check if the selected quantity
                exceeds the available quantity for the product
                """
                if quantity > product.quantity_available:
                    messages.error(
                        request,
                        f"The selected quantity exceeds"
                        f"the available quantity "
                        f"for the product.")
                    return redirect(reverse('basket'))

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

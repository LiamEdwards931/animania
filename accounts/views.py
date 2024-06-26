from django.contrib import messages
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, CustomPasswordChange, AddressForm
from django.contrib.auth import login
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Address
from product.models import ProductReview, Product
from product.forms import ProductReviewForm
from checkout.models import Order, OrderLine
# Create your views here.


@receiver(user_logged_in)
# view to display a log in message
def show_login_message(sender, user, request, **kwargs):
    messages.info(request, f"Welcome to Animania {user.username}")


@receiver(user_logged_out)
# view to display a log out message
def show_logout_message(sender, user, request, **kwargs):
    if user is not None:
        messages.info(
            request,
            f"Goodbye {user.username}, We hope you enjoyed your visit!")


def profile(request):
    # Fetch the addresses associated with the current user
    user = request.user
    addresses = Address.objects.filter(user=user)
    orders = Order.objects.all()
    total_sales = sum(order.grand_total for order in orders)
    processed_order = orders.count()

    # Work out the total profit for the store
    total_profit = 0
    order_lines = OrderLine.objects.all()
    for order_line in order_lines:
        total_profit += order_line.product.profit_amount * order_line.quantity

    context = {
        'user': user,
        'addresses': addresses,
        'total_sales': total_sales,
        'processed_orders': processed_order,
        'total_profit': total_profit,
    }
    return render(request, 'profile.html', context)


def register(request):
    # Creates a custom User
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, f'Your account has been created {user.username}')
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def changePassword(request):
    # View for updating the users password
    user = request.user
    if request.method == 'POST':
        form = CustomPasswordChange(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Password Successfully Updated')
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'user': user,
        'form': form,
    }
    return render(request, 'changepassword.html', context)


def addAddress(request):
    # View for adding new addresses to the users profile
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            # Saves the form and associates the address with the user
            address.save()
            messages.success(request, 'New Address Added')
            return redirect('profile')
    else:
        form = AddressForm()

    context = {
        'form': form
    }
    return render(request, 'newaddress.html', context)


def delete_address(request, address_id):
    # Adds a button to the addresses in the profile.html page to delete
    address = get_object_or_404(Address, id=address_id)
    if request.method == 'POST':
        # Address gets deleted
        address.delete()
        messages.success(request, 'Address deleted successfully')
    else:
        messages.error(request, 'Could not Delete this address')
    return redirect('profile')


def update_address(request, address_id):
    """
    View to update the address
    """
    address = get_object_or_404(Address, id=address_id)

    if request.method == 'POST':
        """
        Populate the form with the existing address data and the new POST data
        """
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            messages.success(request, 'address updated successfully')
            return redirect('profile')
    else:
        # Populate the form with the existing address data
        form = AddressForm(instance=address)

    context = {
        'form': form,
        'address_id': address_id,
    }
    return render(request, 'update_address.html', context)


def my_reviews(request):
    user = request.user
    reviews = ProductReview.objects.filter(created_by=user)
    all_reviews = ProductReview.objects.all()

    context = {
        'reviews': reviews,
        'all_reviews': all_reviews,
    }

    return render(request, 'myreviews.html', context)


def delete_review(request, review_id):
    # Deletes the reviews object that the user has posted.
    review = get_object_or_404(ProductReview, id=review_id)
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'You have successfully deleted this review')
    else:
        messages.error(request, 'Could not delete the selected review')
    return redirect('my_reviews')


def update_review(request, review_id):
    # View to update reviews that users have posted
    review = get_object_or_404(ProductReview, id=review_id)

    if request.method == 'POST':
        """
        Populate the form with the existing
        address data and the new POST data
        """
        form = ProductReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'review updated successfully')
            return redirect('my_reviews')
    else:
        # Populate the form with the existing address data
        form = ProductReviewForm(instance=review)

    context = {
        'form': form,
        'review_id': review_id,
    }
    return render(request, 'update_product_review.html', context)

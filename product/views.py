from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.contrib import messages
from .models import Product, product_banner, ProductReview
from . import forms
from .forms import ProductForm, BannerForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

# Create your views here.

# -------------------Homepage view-------------------------
def index(request):
    """
     Creates a view to render index.html, 
     renders all product and message instances
    """
    messages_to_render = messages.get_messages(request)
    products = Product.objects.all()
    banner = product_banner.objects.all()
    new_products = products.filter(new=True)[:4]
    discount_products = products.filter(discounted=True)[:4]

    context = {
        'products': products,
        'newProducts': new_products,
        'discount_products':discount_products,
        'messages': messages_to_render,
        'banner': banner,
    }
    
    return render(request, 'index.html', context)

# ---Create/update/delete products views (SuperUser only from the profile page)---------
def amendProducts(request):
    """
    Renders the amend Products.html page, 
    Gets all product instances.
    """
    products = Product.objects.all()
    paginator = Paginator(products, 5)

    page_number = request.GET.get('page')
    paginated_table = paginator.get_page(page_number)
    
    context = {
        'products': products,
        'paginated_table': paginated_table,
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
    View to delete all of a product instance on request by a superuser.
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
    View to Edit all of a product instance on request by a superuser.
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


def new_banner(request):
    """Form view to upload a new banner."""
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            series_name = form.cleaned_data.get('series')
            if Product.objects.filter(series=series_name).exists():
                form.save()
                messages.success(request, 'Banner uploaded successfully')
                return redirect('amendProducts')
            else:
                messages.error(request, 'No products for this series available, please add them if you want a banner.')
        else:
            messages.error(request, 'Form data is not valid. Please check the input.')
    else: 
        form = BannerForm()

    context = {
        'form': form
    }
    
    return render(request, 'new_banner.html', context)

# ------------ All products view --------------------------------------

def all_products(request):
    """
    View returning all the product objects to display
    on the all product page
    """
    products = Product.objects.all()
    banners = product_banner.objects.all()
    product_count = products.count()
    query = None
    filtered_series = None
    filtered_categories = None
    new_products = None
    discounted_products = None

    # Product filtering for organising the products on the page
    sort_by = request.GET.get('sort')
    if sort_by == 'A-Z':
        products = products.order_by('series')
    if sort_by == 'Z-A':
        products = products.order_by('-series')
    elif sort_by == 'price low-high':
        products = products.order_by('price')
    elif sort_by == 'price high-low':
        products = products.order_by('-price')
    
    # Product filtering logic for properties in the product: Used some help from boutique ado
    if request.GET:
        if 'discounted' in request.GET:
            discounted_products = Product.objects.filter(discounted=True)
            products = discounted_products
            product_count = discounted_products.count()
        elif 'new' in request.GET:
            new_products = Product.objects.filter(new=True)
            products = new_products
            product_count = new_products.count()
        elif 'series' in request.GET:
            filtered_series = request.GET['series']
            products = products.filter(series=filtered_series)
            product_count = products.count()
        elif 'category' in request.GET:
            filtered_categories = request.GET['category']
            products = products.filter(category=filtered_categories)
            product_count = products.count()
        
                
   # Filtering by search query - taken from boutqiue ado walkthrough
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "Search field is empty!")
            return redirect('allproducts')

        queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(search_tags__icontains=query)
        products = products.filter(queries)
        product_count = products.count()

    page_size = 32
    paginator = Paginator(products,page_size)
    page_number = request.GET.get('page')
    page_product = paginator.get_page(page_number)
    products = page_product

    context = {
        'products': products,
        'banners': banners,
        'product_count': product_count,
        'search_term': query,
        'filtered_series': filtered_series,
        'filtered_categories': filtered_categories,
        'newProducts': new_products,
        'discountedProducts': discounted_products,
        'page_size': page_size,
    }

    return render(request, 'all_products.html', context)


# ------------ Product detail view ---------------------------------------

def product_detail(request, product_id):
    """
    View that uses the product id to highlight details of a project
    """
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.productreview_set.all()
    review_amount = reviews.count()
    # works out the average review score
    total_rating = sum(review.rating for review in reviews)
    if review_amount > 0:
        average_rating = total_rating / review_amount
    else:
        average_rating = 0
    
    context = {
        'product': product,
        'reviews': reviews,
        'review_amount': review_amount,
        'average_rating': average_rating,
    }
    return render(request,'product_detail.html', context)

#------------Product Review Form ------------------------------------------------

def product_review(request, product_id):
    """View that used the product id to leave a review for that product"""

    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = forms.ProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product  
            review.created_by = request.user  
            review.save()
            messages.success(request, 'Review uploaded successfully')
            return redirect('product_details', product_id=product_id)
        else:
            messages.error(request, 'Could not upload your review please double check the inputs')
    else: 
        form = forms.ProductReviewForm()

    context = {
        'form': form,
        'product': product
    }

    return render(request, 'new_product_review.html', context)

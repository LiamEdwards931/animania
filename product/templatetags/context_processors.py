from product.models import Product

def products_context(request):
    products = Product.objects.all()  # Retrieve all products
    return {'products': products}  # Return the products in a dictionary


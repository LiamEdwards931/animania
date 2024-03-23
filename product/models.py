from django.db import models
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal, ROUND_DOWN
from django.contrib.auth.models import User


class Product(models.Model):
   
    image = CloudinaryField('image',blank=True)
    alternative_images = CloudinaryField('image',blank=True)
    name = models.TextField(max_length=40)
    description = models.TextField()
    series = models.TextField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50, blank=True)
    cost_price = models.DecimalField(max_digits=10,null=True, decimal_places=2, validators=[MinValueValidator(0)])
    search_tags = models.CharField(max_length=100, blank=True)
    related_products = models.ManyToManyField('self', blank=True)
    quantity_available = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    new = models.BooleanField(default=None, null=True)
    discounted = models.BooleanField(default=None, null=True)
    discount_amount = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)], null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
    
    @property
    def discounted_price(self):
        # Calculates a new discounted price: {{ product.discounted_price }}
        if self.discounted and self.discount_amount is not None:
            decimal_discount = Decimal(self.discount_amount)
            discount = self.price * (decimal_discount / 100)
            discounted_price = self.price - discount
            return discounted_price.quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        else:
            return None
        
    @property
    def profit_margin(self):
        # Calculates the profit margin of a product: {{ product.profit_margin }}
        if self.discounted:
            margin = self.discounted_price - self.cost_price
            profit_margin_percent = (margin / self.cost_price) * 100
            return profit_margin_percent.quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        
        elif self.price and self.cost_price is not None:
            margin = self.price - self.cost_price
            profit_margin_percent = (margin / self.cost_price) * 100
            return profit_margin_percent.quantize(Decimal('0.01'), rounding=ROUND_DOWN)
        else:
            return None
        
    @property
    def profit_amount(self):
        # Calculates the amount of profit generated per product {{ product.profit_amount }}
        if self.discounted:
            margin = (self.discounted_price - self.cost_price) / self.cost_price
            return round(margin * self.cost_price,2)
        
        elif self.price and self.cost_price:
            margin = (self.price - self.cost_price) / self.cost_price
            return round(margin * self.cost_price, 2)
        else:
            return None
    
    def clean(self):
        # Validation for price and quantity
        super().clean()
        if self.price <= 0:
            raise ValidationError({'price': 'Price must be greater than zero.'})
        if self.quantity_available < 0:
            raise ValidationError({'quantity_available': 'Quantity must be non-negative.'})


class product_banner(models.Model):
    image = CloudinaryField('image')
    series = models.TextField(max_length=30, null=True)

    def __str__(self):
        return self.series


class ProductReview(models.Model):
    title = models.CharField(max_length=50,null=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    rating = (models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)]))
    content = models.CharField(max_length=250)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Size(models.Model):
    SIZE_CHOICES = [
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ]

    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    alternate_size = models.CharField(max_length=10, choices=SIZE_CHOICES, null=True, blank=True)
    size_quantity_available = models.PositiveIntegerField(validators=[MinValueValidator(0)],null=True)

    def __str__(self):
        return self.alternate_size
from django.db import models
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    SIZE_CHOICES = [
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ]
    
    image = CloudinaryField('image',blank=True)
    alternative_images = CloudinaryField('image',blank=True)
    name = models.TextField(max_length=40)
    description = models.TextField()
    series = models.TextField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50, blank=True)
    search_tags = models.CharField(max_length=100, blank=True)
    related_products = models.ManyToManyField('self', blank=True)
    quantity_available = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    new = models.BooleanField(default=None, null=True)
    discounted = models.BooleanField(default=None, null=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def clean(self):
        super().clean()
        if self.price <= 0:
            raise ValidationError({'price': 'Price must be greater than zero.'})
        if self.quantity_available < 0:
            raise ValidationError({'quantity_available': 'Quantity must be non-negative.'})

    
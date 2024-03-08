from django.db import models
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator

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
    price = models.IntegerField(validators=[MinValueValidator(0)])
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    search_tags = models.CharField(max_length=100, blank=True)
    related_products = models.ManyToManyField('self', blank=True)
    quantity_available = models.IntegerField(validators=[MinValueValidator(0)])
    new = models.BooleanField(default=False)
    discounted = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    size = models.CharField(max_length=1, choices=SIZE_CHOICES, null=True)
    
    def __str__(self):
        return self.name


    
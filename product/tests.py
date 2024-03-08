from django.test import TestCase
from product.models import Product
from datetime import date
# Create your tests here.

class ProductModelTests(TestCase):
    def test_string_representation(self):
        product = Product(name='Test Product', price=10)
        self.assertEqual(str(product), 'Test Product')

    def test_product_creation(self):
        today = date.today()
        product = Product.objects.create(name='New Product', price=20)
        self.assertEqual(product.name, 'New Product')
        self.assertEqual(product.description,'Tokyo Ghoul Figure')
        self.assertEqual(product.series,'Tokyo Ghoul')
        self.assertEqual(product.category,'Figure')
        self.assertEqual(product.sub_category,'Toy')
        self.assertEqual(product.quantity_available, 1)
        self.assertEqual(product.price, 20)
        self.assertEqual(product.new, True)
        self.assertEqual(product.discounted, False)
        self.assertEqual(product.created_on, today)
        self.assertEqual(product.related_products, 'Tokyo Ghoul T-shirt')
    
    
class ProductModelTests(TestCase):
    def test_search_tags(self):
        tags = ['figure', 'tokyo ghoul', 'anime figures', 'gift-ideas']
        product = Product.objects.create(name='New Product', price=20, search_tags=', '.join(tags))
        
        retrieved_tags = product.search_tags.split(', ')
        
        for tag in tags:
            self.assertIn(tag, retrieved_tags)

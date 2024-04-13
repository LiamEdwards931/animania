from django.db import models
import uuid
from django.core.validators import MinValueValidator
from product.models import Product, Size
from django.db.models import Sum
from django.conf import settings

# Create your models here.


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=40, null=False, blank=False)
    door_number = models.IntegerField(
        validators=[MinValueValidator(1)], null=True)
    street = models.CharField(max_length=100, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    county = models.CharField(max_length=100, null=True, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    postal_code = models.CharField(max_length=8, null=False, blank=False)
    date = models.DateField(auto_now=True)
    delivery_cost = models.DecimalField(
            max_digits=6, decimal_places=2, null=False, default=0)
    total_cost = models.DecimalField(
            max_digits=6, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        generate a random order number
        """
        return uuid.uuid4().hex.upper()

    def calculate_total(self):
        """
        Calculates the total cost
        """
        self.total_cost = (
                self.lineitems.aggregate(Sum('subtotal'))['subtotal__sum'] or 0
            )
        if self.total_cost < settings.DELIVERY_AMOUNT:
            self.delivery_cost = self.total_cost * settings.DELIVERY_COST / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.total_cost + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """"
        sets the order number if it hasnt been set already
        """

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLine(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False, on_delete=models.CASCADE,
        related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    product_size = models.ForeignKey(Size, null=True,
                                     blank=True, on_delete=models.CASCADE)
    subtotal = models.DecimalField(
        max_digits=6, decimal_places=2, null=False,
        blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        if self.product.discounted:
            self.subtotal = self.product.discounted_price * self.quantity
        else:
            self.subtotal = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'name:{self.product.name} on order {self.order.order_number}'

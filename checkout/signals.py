from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLine

@ receiver(post_save, sender=OrderLine)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update the Order costs based on the Update/Create 
    of Order Line Items.
    """
    instance.order.calculate_total()

@ receiver(post_delete, sender=OrderLine)
def update_on_delete(sender, instance, **kwargs):
    """
    Update the Order costs based on the deletion of 
    Order Line Items.
    """
    instance.order.calculate_total()
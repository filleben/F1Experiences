from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem, Order

#Save Signal
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Updates order total when new line item is added
    """
    print('save signal received!')
    instance.order.update_total()

#Delete Signal
@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Updates order total when new line item is deleted
    """
    print('delete signal received!')
    instance.order.update_total()
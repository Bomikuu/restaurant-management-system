from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import InventoryItem, InventoryItemLog  # noqa


@receiver(post_save, sender=InventoryItem)
def create_new_log(sender, instance, **kwargs):
    print("create inventory item log")

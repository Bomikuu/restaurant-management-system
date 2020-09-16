from django.db import models
from apps.inventory.models import InventoryItem
from apps.soft_delete.models import SoftDeletionModel

optional = {"blank": True, "null": True}


class Product(SoftDeletionModel):
    STATUS_UNAVAILABLE = 0
    STATUS_AVAILABLE = 1
    STATUS_ARCHIVE = 2

    STATUS_CHOICES = (
        (STATUS_UNAVAILABLE, "Unavailable"),
        (STATUS_AVAILABLE, "Available"),
        (STATUS_ARCHIVE, "Archive"),
    )

    name = models.CharField(max_length=100)
    price = models.FloatField(default=0, max_length=10)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES)
    image = models.ImageField(
        verbose_name="Product Image", null=True, blank=True, default=None, upload_to="products/"
    )
    inventoryItem = models.ForeignKey(InventoryItem, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

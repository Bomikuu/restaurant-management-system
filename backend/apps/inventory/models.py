from django.db import models
from apps.soft_delete.models import SoftDeletionModel
from apps.product.models import Product
from apps.user.models import UserProfile


class InventoryItem(SoftDeletionModel):
    STATUS_UNAVAILABLE = 0
    STATUS_AVAILABLE = 1
    STATUS_ARCHIVE = 2

    STATUS_CHOICES = (
        (STATUS_UNAVAILABLE, "Unavailable"),
        (STATUS_AVAILABLE, "Available"),
        (STATUS_ARCHIVE, "Archive"),
    )

    name = models.CharField(max_length=100)
    status = models.IntegerField(choices=STATUS_CHOICES)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(
        verbose_name="InventoryItem Image", null=True, blank=True, default=None, upload_to="inventory-item/"
    )

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class InventoryItemLog(SoftDeletionModel):
    STOCK_IN = "stock in"
    STOCK_OUT = "stock out"

    LOG_TYPE = (
        (STOCK_IN, "stock in"),
        (STOCK_OUT, "stock out")
    )

    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    quantity = models.IntegerField()
    log_type = models.CharField(max_length=20, choices=LOG_TYPE)
    remarks = models.CharField(max_length=100)
    inventory_item = models.ForeignKey(InventoryItem, null=True, on_delete=models.SET_NULL)
    logged_by = models.OneToOneField(UserProfile, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

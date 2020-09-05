from django.db import models
from apps.soft_delete.models import SoftDeletionModel
from apps.user.models import Account
from apps.product.models import Product
from django.core.validators import MaxValueValidator, MinValueValidator

class Order(SoftDeletionModel):
    STATUS_PENDING = 1
    STATUS_READY = 2
    STATUS_PAID = 3

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_READY, "Ready"),
        (STATUS_PAID, "Paid"),
    )

    total_price = models.FloatField(default=0, max_length=10)
    voided_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    cashier = models.ForeignKey(Account, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES)

    def __str__(self):
        return self.name

    def __unicode__(self): 
        return self.name

class OrderLine(SoftDeletionModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    
    def __str__(self):
        return self.name

    def __unicode__(self): 
        return self.name

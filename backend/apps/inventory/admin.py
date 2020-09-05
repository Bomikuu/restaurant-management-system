from django.contrib import admin
from .models import InventoryItem, InventoryItemLog

admin.site.register(InventoryItem)
admin.site.register(InventoryItemLog)

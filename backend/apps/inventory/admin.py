from django.contrib import admin
from .models import InventoryItem, InventoryItemLog


class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "quantity")


class InventoryItemLogAdmin(admin.ModelAdmin):
    list_display = ("name", "timestamp", "quantity", "log_type", "remarks", "inventory_item", "logged_by")


admin.site.register(InventoryItem, InventoryItemAdmin)
admin.site.register(InventoryItemLog, InventoryItemLogAdmin)

from rest_framework import routers
from .views import InventoryItemViewSet, InventoryItemLogViewSet

router = routers.SimpleRouter()
router.register(r'inventory-items', InventoryItemViewSet)
router.register(r'inventory-item-logs', InventoryItemLogViewSet)

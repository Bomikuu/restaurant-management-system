from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import InventoryItem, InventoryItemLog
from .serializers import InventoryItemSerializer, InventoryItemLogSerializer


class InventoryItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

    def stock_in(self, request):
        # add inventory item log
        # call stock in method
        pass

    def stock_out(self, request):
        # add inventory item log
        # call stock in method
        pass


class InventoryItemLogViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = InventoryItemLog.objects.all()
    serializer_class = InventoryItemLogSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import InventoryItem, InventoryItemLog
from .serializers import InventoryItemSerializer, InventoryItemLogSerializer


class InventoryItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

    @action(detail=False, methods=['get'])
    def generate_report(self, request):
        print("generate report")

        # TODO generate report
        inventoryItems = InventoryItem.objects.all()
        serialized_inventoryItems = InventoryItemSerializer(
            inventoryItems, many=True)

        return Response({'inventoryItems': serialized_inventoryItems.data})

    @action(detail=False, methods=['post'])
    def stock_in(self, request):
        InventoryItem.objects.filter(id=request.data['id']).update(
            status=1)  # status == 1 stands for AVAILABLE

        return Response({'status': 'stock in successful'})

    @action(detail=False, methods=['post'])
    def stock_out(self, request):
        InventoryItem.objects.filter(id=request.data['id']).update(
            status=0)  # status == 0 stands for UNAVAILABLE

        return Response({'status': 'stock out successful'})


class InventoryItemLogViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = InventoryItemLog.objects.all()
    serializer_class = InventoryItemLogSerializer

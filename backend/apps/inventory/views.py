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

        return Response({'status': 'report generated'})


class InventoryItemLogViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = InventoryItemLog.objects.all()
    serializer_class = InventoryItemLogSerializer

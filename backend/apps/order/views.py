from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from .models import Order
from .models import OrderLine
from .serializers import OrderSerializer
from .serializers import OrderLineSerializer

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderLineViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = OrderLine.objects.all()
    serializer_class = OrderLineSerializer

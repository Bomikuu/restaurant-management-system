from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
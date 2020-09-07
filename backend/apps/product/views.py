from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def stock_in(self, request):
        # add inventory item log
        # call stock in method
        pass

    def stock_out(self, request):
        # add inventory item log
        # call stock in method
        pass

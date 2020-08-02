from rest_framework import viewsets
import sys
import os
__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(__dir__, '..'))
from models import Account  # noqa: E402
from api.serializers import AccountSerializer  # noqa: E402


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

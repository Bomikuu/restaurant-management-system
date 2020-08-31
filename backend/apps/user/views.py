from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import Group
from .models import Account
from .serializers import AccountSerializer, GroupSerializer


class AccountViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

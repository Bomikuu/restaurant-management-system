from rest_framework import viewsets

from django.contrib.auth.models import Group
from .models import Account
from .serializers import AccountSerializer, GroupSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
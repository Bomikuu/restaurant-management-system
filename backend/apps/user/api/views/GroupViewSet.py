from rest_framework import viewsets
from django.contrib.auth.models import Group
import sys
import os
__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(__dir__, '..'))
from api.serializers import GroupSerializer  # noqa: E402


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

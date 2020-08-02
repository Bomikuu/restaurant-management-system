from django.conf import settings
from django.db import models
import sys
import os
__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(__dir__, '..'))
sys.path.append(os.path.join(__dir__, '..', '..'))
from soft_delete_utils import SoftDeletionModel  # noqa: E402


class UserProfile(SoftDeletionModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile", null=True
    )

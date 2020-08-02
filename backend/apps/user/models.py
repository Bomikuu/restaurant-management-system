from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.db.models import QuerySet
import datetime

optional = {"blank": True, "null": True}


class Account(AbstractUser, SoftDeletionModel):
    username = models.CharField(blank=True, null=True, max_length=100)
    email = models.EmailField(("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.last_name}, {self.first_name} ({self.username})"
        else:
            return self.username

    def __unicode__(self):
        if self.first_name and self.last_name:
            return f"{self.last_name}, {self.first_name} ({self.username})"
        else:
            return self.username

    @property
    def get_display_name(self):
        if self.first_name and self.last_name:
            return f"{self.last_name}, {self.first_name} ({self.username})"
        elif self.username:
            return self.username
        else:
            return ""


class UserProfile(SoftDeletionModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile", null=True
    )

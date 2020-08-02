from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.db.models import QuerySet
import datetime

optional = {"blank": True, "null": True}


class SoftDeletionQuerySet(QuerySet):
    def delete(self):
        return super(SoftDeletionQuerySet, self).update(deleted_at=datetime.datetime.now())

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)


class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


class SoftDeletionModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = datetime.datetime.now()
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()


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

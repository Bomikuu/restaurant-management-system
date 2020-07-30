from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.db.models import QuerySet
from datetime import timezone

optional = {"blank": True, "null": True}


class SoftDeletionQuerySet(QuerySet):
    def delete(self):
        return super(SoftDeletionQuerySet, self).update(deleted_at=timezone.now())

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
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(SoftDeletionModel, self).delete()


class Account(AbstractUser, SoftDeletionModel):
    # class Meta:
    #     permissions = (
    #         ("view_user_list", "Can View User List"),
    #     )

    # override username to set blank and null to True
    username = models.CharField(blank=True, null=True, max_length=100)
    # override email to set unique to True
    email = models.EmailField(("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        if self.first_name and self.last_name:
            return "{}, {} ({})".format(self.last_name, self.first_name, self.username)
        else:
            return self.username

    def __unicode__(self):
        if self.first_name and self.last_name:
            return "{}, {} ({})".format(self.last_name, self.first_name, self.username)
        else:
            return self.username

    @property
    def get_display_name(self):
        if self.first_name and self.last_name:
            return "{}, {} ({})".format(self.last_name, self.first_name, self.username)
        elif self.username:
            return self.username
        else:
            return ""

    def save(self, *args, **kwargs):
        if not self.pk:
            super(Account, self).save(*args, **kwargs)
            # my_group = Group.objects.get(name='group_name')
            # my_group.user_set.add(self)
        else:
            super(Account, self).save(*args, **kwargs)


class UserProfile(SoftDeletionModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile", null=True
    )

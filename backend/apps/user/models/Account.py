from django.contrib.auth.models import AbstractUser
from django.db import models
import sys
import os
__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(__dir__, '..', '..'))
from soft_delete_utils import SoftDeletionModel  # noqa: E402


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

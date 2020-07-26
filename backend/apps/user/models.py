from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.contrib.postgres.fields import JSONField

optional = {"blank": True, "null": True}


class Account(AbstractUser):
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


class UserType(models.Model):
    USER_TYPE_CHOICES = (
        ("Admin", "Admin"),
        ("KitchenDevice", "KitchenDevice"),
        ("CashierDevice", "CashierDevice"),
        ("RestaurantDevice", "RestaurantDevice"),
    )
    type = models.CharField(max_length=20, default="")


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    api_key = models.CharField(max_length=255, **optional)
    extra_info = JSONField(default=dict)
    type = models.ManyToManyField(UserType, related_name="user_types")

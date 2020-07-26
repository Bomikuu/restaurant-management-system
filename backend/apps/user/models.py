from django.contrib.auth.models import AbstractUser, Group

from django.db import models

optional = {"blank": True, "null": True}


class CustomUser(AbstractUser):
    # class Meta:
    #     permissions = (
    #         ("view_user_list", "Can View User List"),
    #     )

    api_key = models.CharField(max_length=255, **optional)

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
            super(CustomUser, self).save(*args, **kwargs)
            # my_group = Group.objects.get(name='group_name')
            # my_group.user_set.add(self)
        else:
            super(CustomUser, self).save(*args, **kwargs)

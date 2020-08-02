from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
import sys
import os
__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(__dir__, '..'))
sys.path.append(os.path.join(__dir__, '..', '..'))
from soft_delete_utils import SoftDeletionAdmin  # noqa: E402
from models import Account, UserProfile  # noqa: E402


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


@admin.register(Account)
class UserAdmin(SoftDeletionAdmin):
    # TODO admin should not be able to see soft deleted objects
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
        }),
    )
    list_display = ("email", "first_name", "last_name", "is_staff")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    inlines = (UserProfileInline,)

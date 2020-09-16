from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Account, UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    exclude = ['deleted_at']


class SoftDeletionAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = self.model.objects.filter(deleted_at__isnull=True)
        # The below is copied from the base implementation in BaseModelAdmin to prevent other changes in behavior
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs

    def delete_model(self, request, obj):
        obj.delete()


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

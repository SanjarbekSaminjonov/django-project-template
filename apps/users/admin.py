from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from rest_framework.authtoken.admin import TokenAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


TokenAdmin.raw_id_fields = ["user"]


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = (
        "phone_number",
        "full_name",
        "date_joined",
        "is_staff",
        "is_superuser",
    )
    list_filter = ("is_staff", "is_superuser", "groups")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "phone_number",
                    "full_name",
                    "extra_data",
                )
            },
        ),
        (
            "Permissions",
            {"fields": ("is_staff", "is_superuser", "groups", "user_permissions")},
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("phone_number", "password1", "password2"),
            },
        ),
    )
    search_fields = ("phone_number", "full_name")
    ordering = ("date_joined",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )

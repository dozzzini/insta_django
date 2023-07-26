from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(UserAdmin):
    # list_display = ("username", "profileIntroduce", "followerNum")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
            (
                ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
            ),
    )
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.account.models import Account


@admin.register(Account)
class AccountAdmin(UserAdmin):
    search_fields = ("email",)
    list_display = ("username", "email", "is_active")
    list_filter = ("is_active",)
    fieldsets = (
        (None, {
            "fields": (
                "first_name",
                "last_name",
                "username",
                "email",
                "password"
            )
        }
         ),
        ("Permissions", {
            "fields": (
                "user_permissions",
                "groups",
                "is_superuser",
                "is_staff"
            )
        }
         ),
        ("Importand Date", {
            "fields": ("last_login",)
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2'), }),)
    readonly_fields = ("password", "last_login")

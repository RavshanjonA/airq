from django.contrib import admin

from apps.monitoring.models import Current


@admin.register(Current)
class CurrentAdmin(admin.ModelAdmin):
    pass
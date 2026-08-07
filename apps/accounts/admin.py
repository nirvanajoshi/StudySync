from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "college",
        "semester",
        "daily_study_goal",
        "created_at",
    )

    search_fields = (
        "user__username",
        "college",
    )

    list_filter = (
        "semester",
    )

    ordering = (
        "user__username",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    list_per_page = 20
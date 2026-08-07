from django.contrib import admin
from .models import Progress


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "subject",
        "completion_percentage",
        "completed_chapters",
        "current_streak",
        "longest_streak",
    )

    search_fields = (
        "user__username",
        "subject__name",
    )

    list_filter = (
        "subject",
    )

    readonly_fields = (
        "updated_at",
    )

    ordering = (
        "-updated_at",
    )

    list_per_page = 20
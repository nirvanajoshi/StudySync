from django.contrib import admin
from .models import DailyPlan, StudySession


@admin.register(DailyPlan)
class DailyPlanAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "date",
        "planned_study_hours",
        "total_available_hours",
        "is_completed",
    )

    search_fields = (
        "user__username",
    )

    list_filter = (
        "is_completed",
        "date",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "-date",
    )

    list_per_page = 20


@admin.register(StudySession)
class StudySessionAdmin(admin.ModelAdmin):
    list_display = (
        "subject",
        "chapter",
        "daily_plan",
        "start_time",
        "end_time",
        "status",
        "priority",
    )

    search_fields = (
        "subject__name",
        "chapter__title",
        "daily_plan__user__username",
    )

    list_filter = (
        "status",
        "priority",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "start_time",
    )

    list_per_page = 20
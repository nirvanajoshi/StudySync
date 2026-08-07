from django.contrib import admin
from .models import Subject, Chapter


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "name",
        "user",
        "difficulty",
        "target_grade",
        "is_active",
    )

    search_fields = (
        "code",
        "name",
        "user__username",
    )

    list_filter = (
        "difficulty",
        "target_grade",
        "is_active",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "code",
    )

    list_per_page = 20


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = (
        "chapter_number",
        "title",
        "subject",
        "estimated_hours",
        "is_completed",
    )

    search_fields = (
        "title",
        "subject__name",
        "subject__code",
    )

    list_filter = (
        "is_completed",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "subject",
        "chapter_number",
    )

    list_per_page = 20
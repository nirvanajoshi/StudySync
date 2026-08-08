from django.contrib import admin
from .models import Note, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "user",
        "color",
        "created_at",
    )

    search_fields = (
        "name",
        "user__username",
    )

    list_filter = (
        "user",
    )

    ordering = (
        "name",
    )

    list_per_page = 20


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
        "subject",
        "is_favorite",
        "updated_at",
    )

    search_fields = (
        "title",
        "user__username",
        "subject__name",
    )

    list_filter = (
        "is_favorite",
        "subject",
    )

    filter_horizontal = (
        "tags",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "-is_favorite",
        "-updated_at",
    )

    list_per_page = 20
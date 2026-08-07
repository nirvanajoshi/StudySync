from django.contrib import admin
from .models import Exam


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "subject",
        "user",
        "exam_date",
        "exam_time",
        "importance",
        "status",
    )

    search_fields = (
        "title",
        "subject__name",
        "user__username",
    )

    list_filter = (
        "importance",
        "status",
        "exam_date",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = (
        "-exam_date",
        "-exam_time",
    )

    list_per_page = 20
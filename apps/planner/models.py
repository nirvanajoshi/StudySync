from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.db import models

from apps.subjects.models import Subject, Chapter


class DailyPlan(models.Model):
    user = models.ForeignKey(User, related_name="daily_plans", on_delete=models.CASCADE)
    date = models.DateField()
    total_available_hours = models.DecimalField(
        max_digits=4, 
        decimal_places=1, 
        validators=[MinValueValidator(0)]
    )
    planned_study_hours = models.DecimalField(
        max_digits=4, 
        decimal_places=1, 
        validators=[MinValueValidator(0)]
    )
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Daily Plan"
        verbose_name_plural = "Daily Plans"
        ordering = ["-date"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "date"],
                name="unique_daily_plan_per_user_per_date"
            )
        ]

    def clean(self):
        super().clean()
        if (
            self.planned_study_hours is not None 
            and self.total_available_hours is not None
            and self.planned_study_hours > self.total_available_hours
        ):
            raise ValidationError({
                "planned_study_hours": "Planned study hours cannot exceed total available hours."
            })

    def __str__(self):
        return f"{self.user.username} - {self.date}"


class StudySession(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("skipped", "Skipped"),
    )

    PRIORITY_CHOICES = (
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    )

    daily_plan = models.ForeignKey(
        DailyPlan,
        related_name="study_sessions",
        on_delete=models.CASCADE,
    )
    subject = models.ForeignKey(
        Subject,
        related_name="study_sessions",
        on_delete=models.CASCADE,
    )
    chapter = models.ForeignKey(
        Chapter,
        related_name="study_sessions",
        on_delete=models.CASCADE,
    )

    start_time = models.TimeField()
    end_time = models.TimeField()

    planned_duration = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        default=1.0,
        validators=[MinValueValidator(0)]
    )
    actual_duration = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        blank=True,
        null=True,
        validators=[MinValueValidator(0)]
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="medium"
    )

    remarks = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Study Session"
        verbose_name_plural = "Study Sessions"
        ordering = ["daily_plan", "start_time"]

    def clean(self):
        super().clean()
        errors = {}

        # Ensure start_time is earlier than end_time
        if self.start_time and self.end_time and self.start_time >= self.end_time:
            errors["end_time"] = "End time must be after start time."

        # Ensure selected chapter belongs to selected subject
        if self.chapter_id and self.subject_id and self.chapter.subject_id != self.subject_id:
            errors["chapter"] = f"Chapter '{self.chapter.title}' does not belong to subject '{self.subject}'."

        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return f"{self.daily_plan.date} | {self.subject.code} - {self.chapter.title}"
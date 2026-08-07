from django.db import models
from django.contrib.auth.models import User


class Exam(models.Model):
    IMPORTANCE_CHOICES = (
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    )

    STATUS_CHOICES = (
        ("upcoming", "Upcoming"),
        ("completed", "Completed"),
        ("missed", "Missed"),
        ("cancelled", "Cancelled"),
    )

    user = models.ForeignKey(
        User,
        related_name="exams",
        on_delete=models.CASCADE
    )

    subject = models.ForeignKey(
        "subjects.Subject",
        related_name="exams",
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    exam_date = models.DateField()
    exam_time = models.TimeField()

    duration = models.DurationField()

    location = models.CharField(
        max_length=200,
        blank=True
    )

    importance = models.CharField(
        max_length=10,
        choices=IMPORTANCE_CHOICES,
        default="medium"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="upcoming"
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Exam"
        verbose_name_plural = "Exams"
        ordering = ["-exam_date", "-exam_time"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "subject", "title", "exam_date"],
                name="unique_exam_per_subject"
            ),
        ]

    def __str__(self):
        return f"{self.title} ({self.subject.code})"
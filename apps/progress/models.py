from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Progress(models.Model):
    user = models.ForeignKey(
        User, 
        related_name="progress_records", 
        on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        "subjects.Subject", 
        related_name="progress_records", 
        on_delete=models.CASCADE
    )
    
    total_study_hours = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0.00,
        validators=[MinValueValidator(0.00)]
    )
    completed_chapters = models.PositiveIntegerField(default=0)
    completion_percentage = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=0.00,
        validators=[MinValueValidator(0.00), MaxValueValidator(100.00)]
    )
    current_streak = models.PositiveIntegerField(default=0)
    longest_streak = models.PositiveIntegerField(default=0)
    
    last_studied = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Progress"
        verbose_name_plural = "Progress Records"
        ordering = ["-updated_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "subject"], 
                name="unique_user_subject_progress"
            )
        ]

    def save(self, *args, **kwargs):
        if self.current_streak > self.longest_streak:
            self.longest_streak = self.current_streak
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.subject.name} ({self.completion_percentage}%)"
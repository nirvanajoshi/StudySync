from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(
        max_length=7,
        default="#6C757D",
        validators=[
            RegexValidator(
                regex=r"^#([A-Fa-f0-9]{6})$",
                message="Enter a valid 6-character hex color code (e.g., #FF5733).",
            )
        ],
        help_text="Hex color code including '#'",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Note(models.Model):
    user = models.ForeignKey(
        User, 
        related_name="notes", 
        on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        "subjects.Subject",
        related_name="notes",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    attachment = models.FileField(
        upload_to="notes/attachments/", 
        blank=True, 
        null=True
    )
    tags = models.ManyToManyField("Tag", related_name="notes", blank=True)
    is_favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
        ordering = ["-is_favorite", "-updated_at"]

    def __str__(self):
        return f"{self.title} ({self.user.username})"
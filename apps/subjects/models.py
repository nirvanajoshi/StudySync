from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    DIFFICULTY_CHOICES = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )
    GRADE_CHOICES = (
        ('A+', 'A+'),
        ('A', 'A'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('D+', 'D+'),
        ('D', 'D'),
        ('F', 'F'),
    )
    user = models.ForeignKey(User,related_name='subjects', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    color = models.CharField(max_length=20,default="#3B82F6")
    target_grade = models.CharField(max_length=10, choices=GRADE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
        ordering = ["code"]
        constraints = [
        models.UniqueConstraint(
            fields=["user", "code"],
            name="unique_subject_code_per_user"
        ),
        models.UniqueConstraint(
            fields=["user", "name"],
            name="unique_subject_name_per_user"
        ),
    ]
        
    def __str__(self):
        return f"{self.code} - {self.name}"
    
class Chapter(models.Model):
    subject = models.ForeignKey(Subject, related_name='chapters', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    chapter_number = models.PositiveSmallIntegerField()
    estimated_hours = models.DecimalField(max_digits=4, decimal_places=1, default=1.0)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Chapter"
        verbose_name_plural = "Chapters"
        ordering = ["chapter_number"]
        constraints = [
            models.UniqueConstraint(
                fields=["subject", "chapter_number"],
                name="unique_chapter_number_per_subject"
            ),
            models.UniqueConstraint(
                fields=["subject", "title"],
                name="unique_chapter_title_per_subject"
            )
        ]

    def __str__(self):
        return f"{self.subject.code} | Chapter {self.chapter_number}: {self.title}"
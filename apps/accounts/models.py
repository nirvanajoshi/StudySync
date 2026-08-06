from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    SEMESTER_CHOICES = [
        (1, '1st Semester'),
        (2, '2nd Semester'),
        (3, '3rd Semester'),
        (4, '4th Semester'),
        (5, '5th Semester'),
        (6, '6th Semester'),
        (7, '7th Semester'),
        (8, '8th Semester'),
    ]
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    college = models.CharField(max_length=100, blank=True)
    semester = models.PositiveSmallIntegerField(blank=True,null=True, choices=SEMESTER_CHOICES)
    daily_study_goal = models.PositiveIntegerField(default=60,help_text="Daily study goal in minutes")
    bio = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ["user__username"]
    
    def __str__(self):
        return self.user.username
    
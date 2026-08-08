from django import forms
from .models import Subject, Chapter


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = [
            "name",
            "code",
            "description",
            "difficulty",
            "color",
            "target_grade",
            "is_active",
        ]


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = [
            "title",
            "chapter_number",
            "estimated_hours",
            "is_completed",
        ]
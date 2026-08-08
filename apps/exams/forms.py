from django import forms
from .models import Exam


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = [
            "subject",
            "title",
            "exam_date",
            "exam_time",
            "duration",
            "location",
            "importance",
            "status",
            "notes",
        ]
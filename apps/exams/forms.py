from django import forms

from apps.subjects.models import Subject

from .models import Exam


class ExamForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        # Only allow the current user's own subjects.
        if user is not None:
            self.fields["subject"].queryset = Subject.objects.filter(
                user=user,
                is_active=True,
            )

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
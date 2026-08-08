from django import forms

from apps.subjects.models import Chapter, Subject

from .models import DailyPlan, StudySession


class DailyPlanForm(forms.ModelForm):
    class Meta:
        model = DailyPlan
        fields = [
            "date",
            "total_available_hours",
            "planned_study_hours",
            "is_completed",
        ]


class StudySessionForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        # Only allow the current user's own subjects and chapters.
        if user is not None:
            self.fields["subject"].queryset = Subject.objects.filter(
                user=user,
                is_active=True,
            )
            self.fields["chapter"].queryset = Chapter.objects.filter(
                subject__user=user,
            )

    class Meta:
        model = StudySession
        fields = [
            "subject",
            "chapter",
            "start_time",
            "end_time",
            "planned_duration",
            "actual_duration",
            "status",
            "priority",
            "remarks",
        ]
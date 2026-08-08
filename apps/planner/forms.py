from django import forms
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
    class Meta:
        model = StudySession
        fields = [
            "daily_plan",
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
from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "profile_picture",
            "college",
            "semester",
            "daily_study_goal",
            "bio",
        ]
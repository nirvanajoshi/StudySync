from django import forms

from apps.subjects.models import Subject

from .models import Note, Tag


class NoteForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        # Restrict selectable subjects and tags to the current user's own.
        if user is not None:
            self.fields["subject"].queryset = Subject.objects.filter(
                user=user,
                is_active=True,
            )
            self.fields["tags"].queryset = Tag.objects.filter(user=user)

    class Meta:
        model = Note
        fields = [
            "subject",
            "title",
            "content",
            "attachment",
            "tags",
            "is_favorite",
        ]


class TagForm(forms.ModelForm):
    color = forms.CharField(
        widget=forms.TextInput(attrs={
            "type": "color",
            "class": "color-input",
        }),
    )

    class Meta:
        model = Tag
        fields = [
            "name",
            "color",
        ]

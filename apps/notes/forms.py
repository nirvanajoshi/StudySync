from django import forms
from .models import Note, Tag


class NoteForm(forms.ModelForm):
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
    class Meta:
        model = Tag
        fields = [
            "name",
            "color",
        ]
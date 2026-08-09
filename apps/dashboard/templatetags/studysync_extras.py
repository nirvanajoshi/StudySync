"""
Shared template filters for StudySync.

Auto-discovered because the dashboard app is in INSTALLED_APPS.
Load in any template with:  {% load studysync_extras %}
"""
from django import template
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.filter
def fmt_duration(value):
    """
    Format a datetime.timedelta (Exam.duration) as "2h 05m".

    Falls back gracefully when the value is None or not a timedelta.
    """
    if value is None:
        return "—"

    try:
        total_minutes = int(value.total_seconds() // 60)
    except AttributeError:
        return value

    hours, minutes = divmod(total_minutes, 60)
    if hours and minutes:
        return f"{hours}h {minutes:02d}m"
    if hours:
        return f"{hours}h"
    return f"{minutes}m"


@register.filter
def profile_picture_url(user):
    """
    Return the user's profile picture URL, or "" when the user has no
    Profile yet / no picture. Safe for users without a Profile row.
    """
    try:
        picture = user.profile.profile_picture
    except (ObjectDoesNotExist, AttributeError):
        return ""

    if picture:
        try:
            return picture.url
        except (ValueError, OSError):
            return ""
    return ""


@register.filter
def fmt_hours(value):
    """
    Format a decimal number of hours (actual_duration, total_study_time)
    as "3.5 hrs" / "1 hr" / "—" when None.
    """
    if value is None:
        return "—"

    try:
        number = float(value)
    except (TypeError, ValueError):
        return value

    unit = "hr" if number == 1 else "hrs"
    if number == int(number):
        return f"{int(number)} {unit}"
    return f"{number:g} {unit}"

from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render
from django.utils import timezone

from apps.exams.models import Exam
from apps.notes.models import Note
from apps.planner.models import DailyPlan, StudySession
from apps.subjects.models import Subject


@login_required
def dashboard_view(request):
    """
    Main display view for the user's dashboard.
    Gathers overview metrics and recent activity across apps.
    """
    user = request.user
    today = timezone.now().date()

    # Overview metrics
    subject_count = Subject.objects.filter(
        user=user,
        is_active=True,
    ).count()

    note_count = Note.objects.filter(user=user).count()

    upcoming_exams = Exam.objects.filter(
        user=user,
        status="upcoming",
        exam_date__gte=today,
    ).order_by("exam_date", "exam_time")[:5]

    today_plans = DailyPlan.objects.filter(
        user=user,
        date=today,
    )

    today_study_time = (
        StudySession.objects.filter(
            daily_plan__user=user,
            daily_plan__date=today,
            status="completed",
        ).aggregate(total=Sum("actual_duration"))["total"]
        or 0
    )

    recent_notes = Note.objects.filter(
        user=user
    ).order_by("-updated_at")[:5]

    context = {
        "user": user,
        "subject_count": subject_count,
        "note_count": note_count,
        "upcoming_exams": upcoming_exams,
        "today_plans": today_plans,
        "today_study_time": today_study_time,
        "recent_notes": recent_notes,
    }

    return render(request, "dashboard/dashboard.html", context)
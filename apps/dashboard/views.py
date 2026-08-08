from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Import models from other apps as needed for dashboard metrics
# from apps.subjects.models import Subject
# from apps.planner.models import DailyPlan
# from apps.exams.models import Exam
# from apps.notes.models import Note


@login_required
def dashboard_view(request):
    """
    Main display view for the user's dashboard.
    Gathers overview metrics and recent activity across apps.
    """
    user = request.user

    # Example aggregated data queries:
    # upcoming_exams = Exam.objects.filter(user=user).order_by('date')[:5]
    # today_plans = DailyPlan.objects.filter(user=user, date=timezone.now().date())
    # recent_notes = Note.objects.filter(user=user).order_by('-created_at')[:5]

    context = {
        "user": user,
        # "upcoming_exams": upcoming_exams,
        # "today_plans": today_plans,
        # "recent_notes": recent_notes,
    }

    return render(request, "dashboard/dashboard.html", context)
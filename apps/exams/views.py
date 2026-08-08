from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q, Sum
from django.shortcuts import get_object_or_404, render

from apps.planner.models import StudySession
from apps.subjects.models import Chapter, Subject


@login_required
def progress_dashboard(request):
    user = request.user

    total_subjects = Subject.objects.filter(
        user=user,
        is_active=True
    ).count()

    total_chapters = Chapter.objects.filter(
        subject__user=user
    ).count()

    completed_chapters = Chapter.objects.filter(
        subject__user=user,
        is_completed=True
    ).count()

    completion_rate = (
        round((completed_chapters / total_chapters) * 100, 1)
        if total_chapters > 0
        else 0
    )

    total_study_time = (
        StudySession.objects.filter(
            daily_plan__user=user
        ).aggregate(
            total=Sum("actual_duration")
        )["total"]
        or 0
    )

    subjects = Subject.objects.filter(
        user=user,
        is_active=True
    ).annotate(
        total_chapters=Count("chapters"),
        completed_chapters=Count(
            "chapters",
            filter=Q(chapters__is_completed=True)
        ),
    )

    context = {
        "total_subjects": total_subjects,
        "total_chapters": total_chapters,
        "completed_chapters": completed_chapters,
        "completion_rate": completion_rate,
        "total_study_time": total_study_time,
        "subjects": subjects,
    }

    return render(
        request,
        "progress/progress_dashboard.html",
        context
    )


@login_required
def subject_progress(request, subject_pk):
    subject = get_object_or_404(
        Subject,
        pk=subject_pk,
        user=request.user
    )

    chapters = subject.chapters.all()

    total_chapters = chapters.count()

    completed_chapters = chapters.filter(
        is_completed=True
    ).count()

    completion_rate = (
        round((completed_chapters / total_chapters) * 100, 1)
        if total_chapters > 0
        else 0
    )

    subject_study_time = (
        StudySession.objects.filter(
            daily_plan__user=request.user,
            subject=subject
        ).aggregate(
            total=Sum("actual_duration")
        )["total"]
        or 0
    )

    context = {
        "subject": subject,
        "chapters": chapters,
        "total_chapters": total_chapters,
        "completed_chapters": completed_chapters,
        "completion_rate": completion_rate,
        "subject_study_time": subject_study_time,
    }

    return render(
        request,
        "progress/subject_progress.html",
        context
    )
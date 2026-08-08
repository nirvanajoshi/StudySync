from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DailyPlanForm, StudySessionForm
from .models import DailyPlan, StudySession


# =========================
# Daily Plan Views
# =========================

@login_required
def planner_view(request):
    daily_plans = DailyPlan.objects.filter(
        user=request.user
    ).order_by("-date")

    return render(
        request,
        "planner/planner.html",
        {"daily_plans": daily_plans}
    )


@login_required
def daily_plan_create(request):
    if request.method == "POST":
        form = DailyPlanForm(request.POST)

        if form.is_valid():
            daily_plan = form.save(commit=False)
            daily_plan.user = request.user
            daily_plan.save()

            messages.success(
                request,
                "Daily plan created successfully!"
            )

            return redirect(
                "planner:daily_plan_detail",
                pk=daily_plan.pk
            )
    else:
        form = DailyPlanForm()

    return render(
        request,
        "planner/daily_plan_form.html",
        {
            "form": form,
            "title": "Create Daily Plan",
        }
    )


@login_required
def daily_plan_detail(request, pk):
    daily_plan = get_object_or_404(
        DailyPlan,
        pk=pk,
        user=request.user
    )

    study_sessions = daily_plan.study_sessions.all()

    return render(
        request,
        "planner/daily_plan_detail.html",
        {
            "daily_plan": daily_plan,
            "study_sessions": study_sessions,
        }
    )


@login_required
def daily_plan_edit(request, pk):
    daily_plan = get_object_or_404(
        DailyPlan,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":
        form = DailyPlanForm(
            request.POST,
            instance=daily_plan
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Daily plan updated successfully!"
            )

            return redirect(
                "planner:daily_plan_detail",
                pk=daily_plan.pk
            )
    else:
        form = DailyPlanForm(instance=daily_plan)

    return render(
        request,
        "planner/daily_plan_form.html",
        {
            "form": form,
            "daily_plan": daily_plan,
            "title": "Edit Daily Plan",
        }
    )


@login_required
def daily_plan_delete(request, pk):
    daily_plan = get_object_or_404(
        DailyPlan,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":
        daily_plan.delete()

        messages.success(
            request,
            "Daily plan deleted successfully!"
        )

        return redirect("planner:planner_view")

    return render(
        request,
        "planner/daily_plan_confirm_delete.html",
        {"daily_plan": daily_plan}
    )


# =========================
# Study Session Views
# =========================

@login_required
def study_session_create(request, plan_pk):
    daily_plan = get_object_or_404(
        DailyPlan,
        pk=plan_pk,
        user=request.user
    )

    if request.method == "POST":
        form = StudySessionForm(request.POST)

        if form.is_valid():
            session = form.save(commit=False)
            session.daily_plan = daily_plan
            session.save()

            messages.success(
                request,
                "Study session added successfully!"
            )

            return redirect(
                "planner:daily_plan_detail",
                pk=daily_plan.pk
            )
    else:
        form = StudySessionForm()

    return render(
        request,
        "planner/study_session_form.html",
        {
            "form": form,
            "daily_plan": daily_plan,
            "title": "Add Study Session",
        }
    )


@login_required
def study_session_edit(request, pk):
    session = get_object_or_404(
        StudySession,
        pk=pk,
        daily_plan__user=request.user
    )

    if request.method == "POST":
        form = StudySessionForm(
            request.POST,
            instance=session
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Study session updated successfully!"
            )

            return redirect(
                "planner:daily_plan_detail",
                pk=session.daily_plan.pk
            )
    else:
        form = StudySessionForm(instance=session)

    return render(
        request,
        "planner/study_session_form.html",
        {
            "form": form,
            "session": session,
            "title": "Edit Study Session",
        }
    )


@login_required
def study_session_delete(request, pk):
    session = get_object_or_404(
        StudySession,
        pk=pk,
        daily_plan__user=request.user
    )

    plan_pk = session.daily_plan.pk

    if request.method == "POST":
        session.delete()

        messages.success(
            request,
            "Study session deleted successfully!"
        )

        return redirect(
            "planner:daily_plan_detail",
            pk=plan_pk
        )

    return render(
        request,
        "planner/study_session_confirm_delete.html",
        {"session": session}
    )
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ExamForm
from .models import Exam


@login_required
def exam_list(request):
    exams = Exam.objects.filter(
        user=request.user
    ).order_by("exam_date", "exam_time")

    return render(
        request,
        "exams/exam_list.html",
        {"exams": exams}
    )


@login_required
def exam_detail(request, pk):
    exam = get_object_or_404(
        Exam,
        pk=pk,
        user=request.user
    )

    return render(
        request,
        "exams/exam_detail.html",
        {"exam": exam}
    )


@login_required
def exam_create(request):
    if request.method == "POST":
        form = ExamForm(request.POST)

        if form.is_valid():
            exam = form.save(commit=False)
            exam.user = request.user
            exam.save()

            messages.success(
                request,
                "Exam scheduled successfully!"
            )

            return redirect(
                "exams:exam_detail",
                pk=exam.pk
            )
    else:
        form = ExamForm()

    return render(
        request,
        "exams/exam_form.html",
        {
            "form": form,
            "title": "Schedule Exam",
        }
    )


@login_required
def exam_edit(request, pk):
    exam = get_object_or_404(
        Exam,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":
        form = ExamForm(
            request.POST,
            instance=exam
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Exam details updated successfully!"
            )

            return redirect(
                "exams:exam_detail",
                pk=exam.pk
            )
    else:
        form = ExamForm(instance=exam)

    return render(
        request,
        "exams/exam_form.html",
        {
            "form": form,
            "exam": exam,
            "title": "Edit Exam",
        }
    )


@login_required
def exam_delete(request, pk):
    exam = get_object_or_404(
        Exam,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":
        exam.delete()

        messages.success(
            request,
            "Exam deleted successfully!"
        )

        return redirect("exams:exam_list")

    return render(
        request,
        "exams/exam_confirm_delete.html",
        {"exam": exam}
    )
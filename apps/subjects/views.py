from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ChapterForm, SubjectForm
from .models import Chapter, Subject


# =========================
# Subject Views
# =========================

@login_required
def subject_list(request):
    subjects = Subject.objects.filter(
        user=request.user,
        is_active=True
    )

    return render(
        request,
        "subjects/subject_list.html",
        {"subjects": subjects}
    )


@login_required
def subject_detail(request, pk):
    subject = get_object_or_404(
        Subject,
        pk=pk,
        user=request.user
    )

    chapters = subject.chapters.all()

    return render(
        request,
        "subjects/subject_detail.html",
        {
            "subject": subject,
            "chapters": chapters,
        }
    )


@login_required
def subject_create(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)

        if form.is_valid():
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()

            messages.success(
                request,
                "Subject created successfully!"
            )

            return redirect(
                "subjects:subject_detail",
                pk=subject.pk
            )
    else:
        form = SubjectForm()

    return render(
        request,
        "subjects/subject_form.html",
        {
            "form": form,
            "title": "Create Subject",
        }
    )


@login_required
def subject_edit(request, pk):
    subject = get_object_or_404(
        Subject,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":
        form = SubjectForm(
            request.POST,
            instance=subject
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Subject updated successfully!"
            )

            return redirect(
                "subjects:subject_detail",
                pk=subject.pk
            )
    else:
        form = SubjectForm(instance=subject)

    return render(
        request,
        "subjects/subject_form.html",
        {
            "form": form,
            "title": "Edit Subject",
        }
    )


@login_required
def subject_delete(request, pk):
    subject = get_object_or_404(
        Subject,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":
        subject.delete()

        messages.success(
            request,
            "Subject deleted successfully!"
        )

        return redirect("subjects:subject_list")

    return render(
        request,
        "subjects/subject_confirm_delete.html",
        {"subject": subject}
    )


# =========================
# Chapter Views
# =========================

@login_required
def chapter_create(request, subject_pk):
    subject = get_object_or_404(
        Subject,
        pk=subject_pk,
        user=request.user
    )

    if request.method == "POST":
        form = ChapterForm(request.POST)

        if form.is_valid():
            chapter = form.save(commit=False)
            chapter.subject = subject
            chapter.save()

            messages.success(
                request,
                "Chapter added successfully!"
            )

            return redirect(
                "subjects:subject_detail",
                pk=subject.pk
            )
    else:
        form = ChapterForm()

    return render(
        request,
        "subjects/chapter_form.html",
        {
            "form": form,
            "subject": subject,
            "title": "Add Chapter",
        }
    )


@login_required
def chapter_detail(request, pk):
    chapter = get_object_or_404(
        Chapter,
        pk=pk,
        subject__user=request.user
    )

    return render(
        request,
        "subjects/chapter_detail.html",
        {"chapter": chapter}
    )


@login_required
def chapter_edit(request, pk):
    chapter = get_object_or_404(
        Chapter,
        pk=pk,
        subject__user=request.user
    )

    if request.method == "POST":
        form = ChapterForm(
            request.POST,
            instance=chapter
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Chapter updated successfully!"
            )

            return redirect(
                "subjects:chapter_detail",
                pk=chapter.pk
            )
    else:
        form = ChapterForm(instance=chapter)

    return render(
        request,
        "subjects/chapter_form.html",
        {
            "form": form,
            "chapter": chapter,
            "title": "Edit Chapter",
        }
    )


@login_required
def chapter_delete(request, pk):
    chapter = get_object_or_404(
        Chapter,
        pk=pk,
        subject__user=request.user
    )

    subject_pk = chapter.subject.pk

    if request.method == "POST":
        chapter.delete()

        messages.success(
            request,
            "Chapter deleted successfully!"
        )

        return redirect(
            "subjects:subject_detail",
            pk=subject_pk
        )

    return render(
        request,
        "subjects/chapter_confirm_delete.html",
        {"chapter": chapter}
    )
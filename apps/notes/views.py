from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm, TagForm
from .models import Note, Tag


# =========================
# Note Views
# =========================

@login_required
def note_list(request):
    notes = Note.objects.filter(
        user=request.user
    ).order_by("-is_favorite", "-updated_at")

    return render(
        request,
        "notes/note_list.html",
        {"notes": notes}
    )


@login_required
def note_detail(request, pk):
    note = get_object_or_404(
        Note,
        pk=pk,
        user=request.user
    )

    return render(
        request,
        "notes/note_detail.html",
        {"note": note}
    )


@login_required
def note_create(request):
    if request.method == "POST":
        form = NoteForm(
            request.POST,
            request.FILES,
            user=request.user,
        )

        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            form.save_m2m()

            messages.success(
                request,
                "Note created successfully!"
            )

            return redirect(
                "notes:note_detail",
                pk=note.pk
            )
    else:
        form = NoteForm(user=request.user)

    return render(
        request,
        "notes/note_form.html",
        {
            "form": form,
            "title": "Create Note",
        }
    )


@login_required
def note_edit(request, pk):
    note = get_object_or_404(
        Note,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":
        form = NoteForm(
            request.POST,
            request.FILES,
            instance=note,
            user=request.user,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Note updated successfully!"
            )

            return redirect(
                "notes:note_detail",
                pk=note.pk
            )
    else:
        form = NoteForm(
            instance=note,
            user=request.user,
        )

    return render(
        request,
        "notes/note_form.html",
        {
            "form": form,
            "note": note,
            "title": "Edit Note",
        }
    )


@login_required
def note_delete(request, pk):
    note = get_object_or_404(
        Note,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":
        note.delete()

        messages.success(
            request,
            "Note deleted successfully!"
        )

        return redirect("notes:note_list")

    return render(
        request,
        "notes/note_confirm_delete.html",
        {"note": note}
    )


# =========================
# Tag Views
# =========================

@login_required
def tag_list(request):
    tags = Tag.objects.filter(
        user=request.user
    )

    return render(
        request,
        "notes/tag_list.html",
        {"tags": tags}
    )


@login_required
def tag_create(request):
    if request.method == "POST":
        form = TagForm(request.POST)

        if form.is_valid():
            tag = form.save(commit=False)
            tag.user = request.user
            tag.save()

            messages.success(
                request,
                "Tag created successfully!"
            )

            return redirect("notes:tag_list")
    else:
        form = TagForm()

    return render(
        request,
        "notes/tag_form.html",
        {
            "form": form,
            "title": "Create Tag",
        }
    )


@login_required
def tag_delete(request, pk):
    tag = get_object_or_404(
        Tag,
        pk=pk,
        user=request.user,
    )

    if request.method == "POST":
        tag.delete()

        messages.success(
            request,
            "Tag deleted successfully!"
        )

        return redirect("notes:tag_list")

    return render(
        request,
        "notes/tag_confirm_delete.html",
        {"tag": tag}
    )
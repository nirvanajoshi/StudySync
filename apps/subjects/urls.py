from django.urls import path
from . import views

app_name = "subjects"

urlpatterns = [
    # Subject URLs
    path("", views.subject_list, name="subject_list"),
    path("create/", views.subject_create, name="subject_create"),
    path("<int:pk>/", views.subject_detail, name="subject_detail"),
    path("<int:pk>/edit/", views.subject_edit, name="subject_edit"),
    path("<int:pk>/delete/", views.subject_delete, name="subject_delete"),

    # Chapter URLs
    path(
        "<int:subject_pk>/chapters/create/",
        views.chapter_create,
        name="chapter_create",
    ),
    path(
        "chapters/<int:pk>/",
        views.chapter_detail,
        name="chapter_detail",
    ),
    path(
        "chapters/<int:pk>/edit/",
        views.chapter_edit,
        name="chapter_edit",
    ),
    path(
        "chapters/<int:pk>/delete/",
        views.chapter_delete,
        name="chapter_delete",
    ),
]
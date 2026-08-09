from django.urls import path
from . import views

app_name = "progress"

urlpatterns = [
    path("", views.progress_dashboard, name="progress_dashboard"),
    path(
        "subject/<int:subject_pk>/",
        views.subject_progress,
        name="subject_progress",
    ),
]
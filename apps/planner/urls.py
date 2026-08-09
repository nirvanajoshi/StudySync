from django.urls import path
from . import views

app_name = "planner"

urlpatterns = [
    # Daily Plan URLs
    path("", views.planner_view, name="planner_view"),
    path("create/", views.daily_plan_create, name="daily_plan_create"),
    path("<int:pk>/", views.daily_plan_detail, name="daily_plan_detail"),
    path("<int:pk>/edit/", views.daily_plan_edit, name="daily_plan_edit"),
    path("<int:pk>/delete/", views.daily_plan_delete, name="daily_plan_delete"),

    # Study Session URLs
    path(
        "<int:plan_pk>/sessions/create/",
        views.study_session_create,
        name="study_session_create",
    ),
    path(
        "sessions/<int:pk>/edit/",
        views.study_session_edit,
        name="study_session_edit",
    ),
    path(
        "sessions/<int:pk>/delete/",
        views.study_session_delete,
        name="study_session_delete",
    ),
]
from django.urls import path
from . import views

app_name = "exams"

urlpatterns = [
    path("", views.exam_list, name="exam_list"),
    path("create/", views.exam_create, name="exam_create"),
    path("<int:pk>/", views.exam_detail, name="exam_detail"),
    path("<int:pk>/edit/", views.exam_edit, name="exam_edit"),
    path("<int:pk>/delete/", views.exam_delete, name="exam_delete"),
]
from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    # Note URLs
    path("", views.note_list, name="note_list"),
    path("create/", views.note_create, name="note_create"),
    path("<int:pk>/", views.note_detail, name="note_detail"),
    path("<int:pk>/edit/", views.note_edit, name="note_edit"),
    path("<int:pk>/delete/", views.note_delete, name="note_delete"),

    # Tag URLs
    path("tags/", views.tag_list, name="tag_list"),
    path("tags/create/", views.tag_create, name="tag_create"),
    path("tags/<int:pk>/delete/", views.tag_delete, name="tag_delete"),
]
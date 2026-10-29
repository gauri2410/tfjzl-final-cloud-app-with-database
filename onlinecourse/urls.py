from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("course/<int:course_id>/", views.course_details, name="course_details"),
    path("submit/<int:course_id>/", views.submit, name="submit"),
    path("lesson/<int:course_id>/submit/", views.submit, name="lesson_submit"),
    path(
        "exam/result/<int:submission_id>/",
        views.show_exam_result,
        name="exam_result",
    ),
    path(
        "show_exam_result/<int:submission_id>/",
        views.show_exam_result,
        name="show_exam_result",
    ),
]

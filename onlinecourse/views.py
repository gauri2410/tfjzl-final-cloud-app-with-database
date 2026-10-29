from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Choice, Course, Enrollment, Submission


def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, "course_details_bootstrap.html", {"course": course})


@login_required
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    questions = list(course.question_set.prefetch_related("choice_set"))
    enrollment, _ = Enrollment.objects.get_or_create(
        user=request.user if request.user.is_authenticated else None,
        course=course,
    )
    if request.method == "POST":
        selected_ids = []
        for question in questions:
            selected_ids.extend(request.POST.getlist(f"question_{question.pk}"))
        selected_choices = Choice.objects.filter(pk__in=selected_ids)
        submission = Submission.objects.create(
            enrollment=enrollment,
        )
        submission.choices.set(selected_choices)
        return redirect("show_exam_result", submission_id=submission.pk)
    return render(request, "exam.html", {"course": course, "questions": questions})


@login_required
def show_exam_result(request, submission_id):
    submission = get_object_or_404(
        Submission.objects.select_related("enrollment__course"), pk=submission_id
    )
    questions = submission.enrollment.course.question_set.prefetch_related("choice_set")
    score = sum(
        question.grade
        for question in questions
        if question.is_get_score(submission.choices.values_list("id", flat=True))
    )
    total = sum(question.grade for question in questions)
    return render(
        request,
        "exam_result.html",
        {
            "submission": submission,
            "score": score,
            "total_questions": total,
            "percentage": round(score / total * 100) if total else 0,
            "questions": questions,
        },
    )

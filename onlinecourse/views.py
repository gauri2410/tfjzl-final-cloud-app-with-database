from django.shortcuts import get_object_or_404, redirect, render

from .models import Course, Lesson, Submission


def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, "course_details_bootstrap.html", {"course": course})


def submit(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    questions = list(lesson.question_set.prefetch_related("choice_set"))
    score = 0
    selected_choices = {}
    if request.method == "POST":
        for question in questions:
            selected = request.POST.get(f"question_{question.pk}")
            selected_choices[str(question.pk)] = selected
            if selected and question.choice_set.filter(
                pk=selected, is_correct=True
            ).exists():
                score += 1
        submission = Submission.objects.create(
            user=request.user if request.user.is_authenticated else None,
            lesson=lesson,
            score=score,
            total_questions=len(questions),
            selected_choices=selected_choices,
        )
        return redirect("show_exam_result", submission_id=submission.pk)
    return render(request, "exam.html", {"lesson": lesson, "questions": questions})


def show_exam_result(request, submission_id):
    submission = get_object_or_404(
        Submission.objects.select_related("lesson", "user"), pk=submission_id
    )
    return render(
        request,
        "exam_result.html",
        {
            "submission": submission,
            "score": submission.score,
            "total_questions": submission.total_questions,
            "percentage": submission.percentage,
            "selected_choices": submission.selected_choices,
        },
    )

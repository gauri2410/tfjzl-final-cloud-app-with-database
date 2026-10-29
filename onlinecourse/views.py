from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .models import Choice, Course, Enrollment, Learner, Question, Submission


def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, "course_details_bootstrap.html", {"course": course})


def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    default_user, _ = User.objects.get_or_create(
        username="demo_learner", defaults={"email": "demo@example.com"}
    )
    learner, _ = Learner.objects.get_or_create(user=default_user)
    enrollment, _ = Enrollment.objects.get_or_create(
        course=course, learner=learner
    )
    if request.method == "POST":
        selected_ids = []
        for key, value in request.POST.items():
            if key.startswith("choice_"):
                selected_ids.append(value)
        selected_choices = Choice.objects.filter(pk__in=selected_ids)
        submission = Submission.objects.create(
            enrollment=enrollment,
        )
        submission.choices.set(selected_choices)
        return redirect(
            "show_exam_result",
            course_id=course.pk,
            submission_id=submission.pk,
        )
    questions = list(
        Question.objects.filter(lesson__course=course).prefetch_related("choices")
    )
    return render(request, "exam.html", {"course": course, "questions": questions})


def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(
        Submission, pk=submission_id, enrollment__course=course
    )
    selected_ids = set(submission.choices.values_list("id", flat=True))
    questions = Question.objects.filter(lesson__course=course).prefetch_related("choices")
    total = 0
    score = 0
    question_results = []
    for question in questions:
        question_choices = list(question.choices.all())
        correct = [choice for choice in question_choices if choice.is_correct]
        selected = [choice for choice in question_choices if choice.id in selected_ids]
        is_correct = question.is_get_score(selected_ids)
        total += question.grade
        if is_correct:
            score += question.grade
        question_results.append({
            "question_text": question.question_text,
            "selected_answers": [choice.choice_text for choice in selected],
            "correct_answers": [choice.choice_text for choice in correct],
            "is_correct": is_correct,
            "grade": question.grade,
        })
    return render(
        request,
        "exam_result_bootstrap.html",
        {
            "course": course,
            "submission": submission,
            "total_score": score,
            "possible_score": total,
            "selected_ids": selected_ids,
            "grade": score,
            "possible": total,
            "earned": score,
            "total": total,
            "passed": total > 0 and score / total >= 0.6,
            "question_results": question_results,
        },
    )

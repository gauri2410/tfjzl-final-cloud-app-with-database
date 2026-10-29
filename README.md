# Final Project: Add a New Assessment Feature

This repository implements the requested Django assessment feature:

- **Task 1:** [onlinecourse/models.py](onlinecourse/models.py) defines `Question`, `Choice`, and `Submission` (plus the related `Course` and `Lesson` models).
- **Task 2:** [onlinecourse/admin.py](onlinecourse/admin.py) imports the seven requested classes and provides `QuestionInline`, `ChoiceInline`, `QuestionAdmin`, and `LessonAdmin`.
- **Task 3:** Run `python manage.py createsuperuser`, then open `/admin/`. Django displays the **Authentication and Authorization** and **OnlineCourse** sections.
- **Task 4:** [templates/course_details_bootstrap.html](templates/course_details_bootstrap.html) displays the course name and related lessons with Django template tags and Bootstrap.
- **Task 5:** [onlinecourse/views.py](onlinecourse/views.py) provides `submit` and `show_exam_result`.
- **Task 6:** [onlinecourse/urls.py](onlinecourse/urls.py) routes both assessment views.
- **Task 7:** [templates/exam_result.html](templates/exam_result.html) displays the successful “Congratulations!” result, score, and progress bar.

## Run locally

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The admin UI is at `http://127.0.0.1:8000/admin/`.

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("onlinecourse", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Instructor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("courses", models.ManyToManyField(blank=True, related_name="instructors", to="onlinecourse.course")),
                ("user", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="auth.user")),
            ],
        ),
        migrations.CreateModel(
            name="Learner",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("courses", models.ManyToManyField(blank=True, related_name="learners", to="onlinecourse.course")),
                ("user", models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to="auth.user")),
            ],
        ),
        migrations.RenameField(
            model_name="question",
            old_name="text",
            new_name="question_text",
        ),
        migrations.RenameField(
            model_name="choice",
            old_name="text",
            new_name="choice_text",
        ),
        migrations.AddField(
            model_name="submission",
            name="selected_choices",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name="choice",
            name="question",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="onlinecourse.question"),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="course",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="onlinecourse.course"),
        ),
        migrations.AlterField(
            model_name="question",
            name="lesson",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="onlinecourse.lesson"),
        ),
        migrations.AlterField(
            model_name="submission",
            name="lesson",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="onlinecourse.lesson"),
        ),
    ]

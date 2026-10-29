from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import now


class Migration(migrations.Migration):
    dependencies = [("onlinecourse", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Instructor",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_time", models.BooleanField(default=True)),
                ("total_learners", models.IntegerField(default=0)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="Learner",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("occupation", models.CharField(default="student", max_length=20)),
                ("social_link", models.URLField(blank=True, max_length=200)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="Enrollment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date_enrolled", models.DateField(default=now)),
                ("mode", models.CharField(choices=[("AUDIT", "Audit"), ("HONOR", "Honor"), ("BETA", "BETA")], default="AUDIT", max_length=5)),
                ("rating", models.FloatField(default=5.0)),
                ("course", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="onlinecourse.course")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(model_name="question", name="lesson"),
        migrations.RemoveField(model_name="question", name="order"),
        migrations.AddField(
            model_name="question",
            name="course",
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to="onlinecourse.course"),
            preserve_default=False,
        ),
        migrations.AlterField(model_name="question", name="text", field=models.CharField(max_length=150)),
        migrations.AlterField(model_name="choice", name="text", field=models.CharField(max_length=150)),
        migrations.RemoveField(model_name="submission", name="user"),
        migrations.RemoveField(model_name="submission", name="lesson"),
        migrations.RemoveField(model_name="submission", name="score"),
        migrations.RemoveField(model_name="submission", name="total_questions"),
        migrations.RemoveField(model_name="submission", name="submitted_at"),
        migrations.AddField(
            model_name="submission",
            name="enrollment",
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to="onlinecourse.enrollment"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="submission",
            name="choices",
            field=models.ManyToManyField(to="onlinecourse.choice"),
        ),
    ]

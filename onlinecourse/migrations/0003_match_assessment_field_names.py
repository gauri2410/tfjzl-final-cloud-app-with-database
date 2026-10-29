from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("onlinecourse", "0002_add_assessment_models")]

    operations = [
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
        migrations.AlterField(
            model_name="question",
            name="grade",
            field=models.IntegerField(default=1),
        ),
    ]

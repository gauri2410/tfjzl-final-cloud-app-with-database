from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("onlinecourse", "0003_match_assessment_field_names")]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="question_text",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="question",
            name="grade",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="choice",
            name="choice_text",
            field=models.CharField(max_length=500),
        ),
    ]

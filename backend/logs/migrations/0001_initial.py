# Generated by Django 3.1.7 on 2021-04-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("exercises", "0002_remove_exercise_muscle")]

    operations = [
        migrations.CreateModel(
            name="WorkoutLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("monday", "Monday"),
                            ("tuesday", "Tuesday"),
                            ("wednesday", "Wednesday"),
                            ("thursday", "Thursday"),
                            ("friday", "Friday"),
                            ("saturday", "Saturday"),
                            ("sunday", "Sunday"),
                        ],
                        max_length=225,
                    ),
                ),
                ("summary", models.TextField(blank=True, max_length=1500)),
                (
                    "goal",
                    models.CharField(
                        choices=[
                            ("BU", "Bulking"),
                            ("CU", "Cutting"),
                            ("MA", "Maintaining"),
                        ],
                        default="MA",
                        max_length=2,
                    ),
                ),
                ("date", models.DateField(auto_now_add=True, max_length=223)),
                (
                    "muscles",
                    models.CharField(
                        choices=[
                            ("Calves", "Calves"),
                            ("Hamstrings", "Hamstrings"),
                            ("quads", "Quadriceps(quads)"),
                            ("glutes", "Glutes"),
                            ("biceps", "Biceps"),
                            ("triceps", "Triceps"),
                            ("forearms", "Forearms"),
                            ("traps", "Trapezius(traps)"),
                        ],
                        default=None,
                        max_length=100,
                    ),
                ),
                ("exercises", models.ManyToManyField(to="exercises.ExerciseSet")),
            ],
        )
    ]

from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    duration = models.PositiveIntegerField(help_text="Duration in minutes", blank=True, null=True)

    def __str__(self):
        return self.name


class ExerciseSet(models.Model):
    name = models.CharField(max_length=100)
    exercises = models.ManyToManyField(Exercise, related_name="sets")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Set(models.Model):
    exercise_set = models.ForeignKey(ExerciseSet, on_delete=models.CASCADE, related_name="sets")
    repetitions = models.PositiveIntegerField()
    rest_time = models.PositiveIntegerField(help_text="Rest time in seconds", blank=True, null=True)

    def __str__(self):
        return f"{self.exercise_set.name} - {self.repetitions} reps"
# Generated by Django 3.1.7 on 2021-04-26 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("logs", "0002_auto_20210426_1223"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workoutlog",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="userlog",
                to=settings.AUTH_USER_MODEL,
            ),
        )
    ]

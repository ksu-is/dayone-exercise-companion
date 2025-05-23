from django.urls import path
from .views import WorkoutLogCreateView, WorkoutLogView

app_name = "logs"

urlpatterns = [
    path("log_form/", WorkoutLogCreateView.as_view(), name="log_create"),
    path("<str:username>/", WorkoutLogView.as_view(), name="log_list"),
]

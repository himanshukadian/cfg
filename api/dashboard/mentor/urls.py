from django.urls import path

from api.dashboard.mentor.views import MentorView

urlpatterns = [
    path('mentorprofile/', MentorView.as_view()),
]

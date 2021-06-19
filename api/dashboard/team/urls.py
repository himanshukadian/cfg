from django.urls import path

from api.dashboard.team.views import TeamView

urlpatterns = [
    path('teamprofile/', TeamView.as_view()),
]

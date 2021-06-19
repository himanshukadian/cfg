from django.urls import path

from api.dashboard.team.views import TeamView, TeamMemberView

urlpatterns = [
    path('teamprofile/', TeamView.as_view()),
    path('teammemberprofile/', TeamMemberView.as_view()),
]

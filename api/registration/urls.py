from django.urls import path

from api.registration.views import TeamRegisterView, TeamMemberRegisterView\
    # , MentorRegisterView

urlpatterns = [
    path('team/', TeamRegisterView.as_view(), name='team_registration'),
    path('teammember/', TeamMemberRegisterView.as_view(), name='team_member_registration'),
    # path('mentor/', MentorRegisterView.as_view(), name='mentor_registration'),
]

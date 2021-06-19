from django.urls import path, include

urlpatterns = [
    path('team/', include('api.dashboard.team.urls')),
    path('mentor/', include('api.dashboard.mentor.urls')),
]

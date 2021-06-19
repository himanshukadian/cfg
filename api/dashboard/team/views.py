from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cfg.permissions import *
from api.dashboard.team.serializers import TeamSerializer, TeamMemberSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class TeamView(generics.RetrieveUpdateAPIView):
    """View To View Or Update User Profile"""
    serializer_class = TeamSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, UserIsTeamOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def retrieve(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
        print(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = request.user
        # Disabling The Updation Of Username
        # mutable = request.data._mutable
        # request.data._mutable = True
        request.data['username'] = instance.username
        # request.data._mutable = mutable
        serializer = TeamSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response(serializer.data)


class TeamMemberView(generics.RetrieveUpdateAPIView):
    """View To View Or Update User Profile"""
    serializer_class = TeamMemberSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, UserIsTeamMemberOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

    def retrieve(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
        print(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = request.user
        # Disabling The Updation Of Username
        # mutable = request.data._mutable
        # request.data._mutable = True
        request.data['username'] = instance.username
        # request.data._mutable = mutable
        serializer = TeamMemberSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response(serializer.data)



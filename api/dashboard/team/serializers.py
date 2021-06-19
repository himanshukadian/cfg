from rest_framework import serializers
from team.models import Team, TeamMember
from django.contrib.auth import get_user_model

User = get_user_model()


class TeamSerializer(serializers.ModelSerializer):
    """Serializer To Show User Profile In User Dashboard"""

    contact_no = serializers.CharField(
        source='team.contact_no', allow_blank=True, allow_null=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
                  'contact_no']

    def update(self, instance, validated_data):
        """Overwriting The Default update Method For This Serializer
        To Update User And UserProfile At A Single Endpoint"""

        profile_data = validated_data.pop('team', None)
        self.update_or_create_profile(instance, profile_data)
        return super(TeamSerializer, self).update(instance, validated_data)

    def update_or_create_profile(self, user, profile_data):
        """This always creates a Profile if the User is missing one"""
        Team.objects.update_or_create(user=user, defaults=profile_data)




class TeamMemberSerializer(serializers.ModelSerializer):
    """Serializer To Show User Profile In User Dashboard"""

    name = serializers.CharField(
        source='teammember.name', allow_blank=True, allow_null=True)
    school = serializers.CharField(
        source='teammember.school', allow_blank=True, allow_null=True)
    city = serializers.CharField(
        source='teammember.city', allow_blank=True, allow_null=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
                  'name', 'school', 'city']

    def update(self, instance, validated_data):
        """Overwriting The Default update Method For This Serializer
        To Update User And UserProfile At A Single Endpoint"""

        profile_data = validated_data.pop('teammember', None)
        self.update_or_create_profile(instance, profile_data)
        return super(TeamMemberSerializer, self).update(instance, validated_data)

    def update_or_create_profile(self, user, profile_data):
        """This always creates a Profile if the User is missing one"""
        TeamMember.objects.update_or_create(user=user, defaults=profile_data)

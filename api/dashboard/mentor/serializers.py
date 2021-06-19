from rest_framework import serializers
from mentor.models import Mentor
from django.contrib.auth import get_user_model

User = get_user_model()


class MentorSerializer(serializers.ModelSerializer):
    """Serializer To Show User Profile In User Dashboard"""

    bio = serializers.CharField(
        source='mentor.bio', allow_blank=True, allow_null=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
                  'bio']

    def update(self, instance, validated_data):
        """Overwriting The Default update Method For This Serializer
        To Update User And UserProfile At A Single Endpoint"""
        profile_data = validated_data.pop('mentor', None)
        self.update_or_create_profile(instance, profile_data)
        return super(MentorSerializer, self).update(instance, validated_data)

    def update_or_create_profile(self, user, profile_data):
        """This always creates a Profile if the User is missing one"""
        Mentor.objects.update_or_create(user=user, defaults=profile_data)

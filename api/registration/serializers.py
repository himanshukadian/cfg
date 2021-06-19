from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer


class MyCustomRegistrationSerializer(RegisterSerializer):
    TEAM = '0'
    TEAMMEMBER = '1'
    MENTOR = '2'
    USER_TYPE_CHOICES = (
        (TEAM, "Team"),
        (TEAMMEMBER, "Team Member"),
        (MENTOR, "Mentor"),
    )
    user_type = serializers.ChoiceField(choices=USER_TYPE_CHOICES, read_only=True)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['user_type'] = self.validated_data.get('user_type', '')
        return data_dict

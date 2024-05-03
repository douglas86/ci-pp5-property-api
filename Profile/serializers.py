from rest_framework import serializers

from Profile.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    snippets = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = ['user', 'profile_picture']

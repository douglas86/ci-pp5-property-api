from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = ['id', 'user', 'profile_picture', 'created_at', 'updated_at']


class ChangePasswordSerializer(serializers.Serializer):
    """
    This serializer is used to change password.
    Taking in the old password and replacing it with new one.
    """

    # These two serializers will show on the form
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

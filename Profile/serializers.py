from rest_framework import serializers
from adrf.serializers import Serializer

from .models import Profile


class ProfileSerializer(Serializer):
    user = serializers.ReadOnlyField(source='user.username')
    profile_picture = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()

    def get_profile_picture(self, obj):
        return obj.profile_picture.url

    def get_role(self, obj):
        if obj.user.is_superuser:
            return "admin"
        else:
            return obj.role

    # class Meta:
    #     model = Profile
    #     fields = ['id', 'user', 'profile_picture', 'created_at', 'updated_at']


# class ProfileSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source='user.username')
#
#     class Meta:
#         model = Profile
#         fields = ['id', 'user', 'profile_picture', 'created_at', 'updated_at']


class ChangePasswordSerializer(serializers.Serializer):
    """
    This serializer is used to change password.
    Taking in the old password and replacing it with new one.
    """

    # These two serializers will show on the form
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

from rest_framework import serializers
from adrf.serializers import Serializer

from .models import Profile


class ProfileSerializer(Serializer):
    """
    Serializer class for a Profile model.
    """

    user = serializers.ReadOnlyField(source='user.username')
    profile_picture = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()

    def get_profile_picture(self, obj):
        """
        Get Profile URL from a database
        :param obj:
        :return:
        """

        return obj.profile_picture.url

    def get_role(self, obj):
        """
        Returns the role of a user if it is a superuser or not
        :param obj:
        :return:
        """

        if obj.user.is_superuser:
            return "admin"
        else:
            return obj.role


class ChangePasswordSerializer(serializers.Serializer):
    """
    This serializer is used to change password.
    Taking in the old password and replacing it with new one.
    """

    # These two serializers will show on the form
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

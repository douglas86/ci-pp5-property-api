import asyncio

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.admin import User
from adrf.viewsets import ViewSet
from asgiref.sync import async_to_sync

from .models import Profile
from .serializers import ProfileSerializer, ChangePasswordSerializer


# Create your views here.
class ProfileView(ViewSet):
    """
    View all Profiles in database
    """

    model = Profile
    pk = None
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)

    # authentication_classes = (TokenAuthentication, SessionAuthentication)

    async def async_generator(self):
        """
        Generates all Profiles in database using async generator
        :return:
        """

        if self.pk is None:
            profiles = self.model.objects.all()
        else:
            profiles = self.model.objects.filter(pk=self.pk)

        yield profiles

    async def async_coroutine(self):
        """
        Iterate over all Profiles in database from async generator
        :return:
        """

        async for profile in self.async_generator():
            return profile

    async def main(self):
        """
        Awaits all Profiles in database from async coroutine
        :return:
        """

        task = asyncio.create_task(self.async_coroutine())
        return await task

    def retrieve(self, request, pk=None):
        """
        Retrieve all Profiles from a database for viewing
        If pk is given retrieve profile by id
        :param pk: primary key or id of profile
        :param request: data to be returned
        :return:
        """

        self.pk = pk
        data = asyncio.run(self.main())
        serializer = ProfileSerializer(data, many=True, context={'request', request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class ChangePassword(APIView):
    """
    This view is used for changing passwords
    """

    model = Profile
    # serializer needed for serializing to json data
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        # fetches data serializers form
        serializer = self.serializer_class(data=request.data)

        # if the form is valid data
        if serializer.is_valid():
            # change the password based on the current user
            user = request.user

            # passwords fetched from serializer form
            old_password = serializer.validated_data.get('old_password')
            new_password = serializer.validated_data.get('new_password')

            # check if old password is correct
            if not user.check_password(old_password):
                return Response({'old_password': ['Wrong password']}, status=status.HTTP_400_BAD_REQUEST)

            # form to be submitted
            #  new_password1 and new_password2 as the same to pass validation checks
            form = PasswordChangeForm(user, {'old_password': old_password, 'new_password1': new_password,
                                             'new_password2': new_password})

            # run only if the form is the correct data
            # once form is correct then save the new password
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)
            else:
                return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

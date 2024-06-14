import asyncio

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.admin import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from adrf.viewsets import ViewSet
from asgiref.sync import async_to_sync

from .models import Profile
from .serializers import ProfileSerializer, ChangePasswordSerializer
from property.views import AsyncViewSet


class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        return request.user.is_superuser


class LoginView(ViewSet):
    model = Profile.objects.all()
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [JWTAuthentication]
    username = None
    password = None
    pk = None
    message = 'You have successfully logged in!'
    error_message = 'The credentials entered are incorrect'

    def get_profile(self):
        profile = AsyncViewSet(self.model).retrieve()
        return profile

    def search(self, serializer):
        return [element for element in serializer.data if element['user'] == self.username]

    def checks(self, request):
        user = authenticate(username=self.username, password=self.password)

        if user is None:
            return {'message': self.error_message, 'status': status.HTTP_404_NOT_FOUND}
        else:
            self.pk = user.id
            serializer = ProfileSerializer(instance=self.get_profile(), many=True, context={'request': request})
            return {'message': self.message, 'status': status.HTTP_200_OK,
                    'profile': self.search(serializer)}

    def retrieve(self, request):
        self.username = request.POST['username']
        self.password = request.POST['password']

        return Response(self.checks(request))


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

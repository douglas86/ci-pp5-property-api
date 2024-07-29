from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from adrf.viewsets import ViewSet
from rest_framework.views import APIView

from .models import Profile
from .serializers import ProfileSerializer, ChangePasswordSerializer
from property.views import AsyncViewSet, IsSuperUser


class LogoutView(APIView):
    """
    Logout user and block refresh token
    """

    message = 'You have successfully logged out!'

    def post(self, request):
        return self.logout(request)

    def logout(self, request):
        refresh = request.headers.get("refresh")
        print('refresh', refresh)
        refresh_token = RefreshToken(refresh)
        refresh_token.blacklist()

        return Response({'message': self.message, 'status': status.HTTP_200_OK})


class ProfileByIdView(ViewSet):
    """
    Get profile by id
    """

    model = Profile

    serializer_class = ProfileSerializer

    authentication_classes = [TokenAuthentication, SessionAuthentication]

    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        print("pk", type(pk))
        profile = self.model.objects.filter(user_id=pk)
        serializer = self.serializer_class(instance=profile, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileDeleteView(ViewSet):
    """
    Delete profile by id
    """
    model = Profile

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    message = 'You have successfully deleted your profile!'
    error_message = 'Something went wrong, please try again.'

    def destroy(self, request, pk=None):
        profile = self.model.objects.get(user_id=pk)
        user = User.objects.get(pk=pk)

        try:
            profile.delete()
            user.delete()
            return Response({'message': self.message, 'status': status.HTTP_200_OK})
        except profile.DoesNotExist:
            return Response({'message': self.error_message, 'status': status.HTTP_404_NOT_FOUND})


class ProfileListView(ViewSet):
    """
    Get all profiles
    """

    model = Profile
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    message = 'You have successfully fetched data from database'
    error_message = 'There was an error fetching data from database'

    def get_profiles(self, request):
        try:
            profile = self.model.objects.all()
            serializer = ProfileSerializer(instance=profile, many=True, context={'request': request})
            return {'message': self.message, 'status': status.HTTP_200_OK,
                    'profile': serializer.data}
        except AssertionError:
            return {'message': self.error_message, 'status': status.HTTP_404_NOT_FOUND}

    def retrieve(self, request):
        return Response(self.get_profiles(request))


class ChangePasswordView(ViewSet):
    """
    Changing password based on username
    """

    model = Profile
    serializer_class = ChangePasswordSerializer

    success_message = 'You have successfully changed password'
    error_message = 'There was an error changing password'
    field_error_message = 'All fields are required'

    status_200 = status.HTTP_200_OK
    status_400 = status.HTTP_400_BAD_REQUEST

    def change_password(self, request):
        """
        Logic to change password
        :param request:
        :return:
        """

        serializer = ChangePasswordSerializer(data=request.data)
        try:
            username = request.data['username']

            if serializer.is_valid():
                user = AsyncViewSet(User.objects.get(username=username)).retrieve()
                if not user.check_password(serializer.validated_data['old_password']):
                    return Response({'message': self.error_message, 'status': self.status_400})

                user.set_password(serializer.validated_data['new_password'])
                user.save()
                return Response({'message': self.success_message, 'status': self.status_200})
        except KeyError:
            return Response({'message': self.field_error_message, 'status': self.status_400})

    def retrieve(self, request):
        """
        Send response to request
        :param request:
        :return:
        """

        return self.change_password(request)

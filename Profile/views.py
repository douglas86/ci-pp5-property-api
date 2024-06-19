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
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)

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
        profile = AsyncViewSet(self.model.objects.filter(user_id=pk)).retrieve()
        serializer = self.serializer_class(instance=profile, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfileListView(ViewSet):
    """
    Get all profiles
    """

    model = Profile.objects.all()
    permission_classes = [IsAuthenticated, IsSuperUser]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    message = 'You have successfully fetched data from database'
    error_message = 'There was an error fetching data from database'

    def get_profiles(self, request):
        try:
            profile = AsyncViewSet(self.model).retrieve()
            serializer = ProfileSerializer(instance=profile, many=True, context={'request': request})
            return {'message': self.message, 'status': status.HTTP_200_OK,
                    'profile': serializer.data}
        except AssertionError:
            return {'message': self.error_message, 'status': status.HTTP_404_NOT_FOUND}

    def retrieve(self, request):
        return Response(self.get_profiles(request))


class ChangePasswordView(ViewSet):
    """
    Change a password from new to old password
    """

    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def change_password(self, request):
        serializer = self.serializer_class(data=request.data)
        user = request.user

        if serializer.is_valid():
            if not user.check_password(serializer.validated_data['old_password']):
                return Response({'message': 'There was an error with the password that you entered',
                                 'status': status.HTTP_400_BAD_REQUEST})

            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'message': 'You have successfully changed your password', 'status': status.HTTP_200_OK})

        return Response({'message': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})

    def retrieve(self, request):
        return self.change_password(request)

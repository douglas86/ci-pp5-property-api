# import asyncio
#
# from django.contrib.auth import authenticate, logout
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from adrf.viewsets import ViewSet
from rest_framework.views import APIView
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
#
from .models import Profile
from .serializers import ProfileSerializer  # ChangePasswordSerializer
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

# class ChangePassword(APIView):
#     """
#     This view is used for changing passwords
#     """
#
#     model = Profile
#     # serializer needed for serializing to json data
#     serializer_class = ChangePasswordSerializer
#
#     def post(self, request):
#         # fetches data serializers form
#         serializer = self.serializer_class(data=request.data)
#
#         # if the form is valid data
#         if serializer.is_valid():
#             # change the password based on the current user
#             user = request.user
#
#             # passwords fetched from serializer form
#             old_password = serializer.validated_data.get('old_password')
#             new_password = serializer.validated_data.get('new_password')
#
#             # check if old password is correct
#             if not user.check_password(old_password):
#                 return Response({'old_password': ['Wrong password']}, status=status.HTTP_400_BAD_REQUEST)
#
#             # form to be submitted
#             #  new_password1 and new_password2 as the same to pass validation checks
#             form = PasswordChangeForm(user, {'old_password': old_password, 'new_password1': new_password,
#                                              'new_password2': new_password})
#
#             # run only if the form is the correct data
#             # once form is correct then save the new password
#             if form.is_valid():
#                 user = form.save()
#                 update_session_auth_hash(request, user)
#                 return Response({'message': 'Password changed successfully'}, status=status.HTTP_200_OK)
#             else:
#                 return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

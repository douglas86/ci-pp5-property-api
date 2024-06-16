import asyncio

from django.contrib.auth import authenticate, logout
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from adrf.viewsets import ViewSet

from .models import Profile
from .serializers import ProfileSerializer, ChangePasswordSerializer, TokenSerializer
from property.views import AsyncViewSet, IsSuperUser


class LoginView(ViewSet):
    model = Profile.objects.all()
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

        try:
            self.username = request.POST['username']
            self.password = request.POST['password']

            return Response(self.checks(request))
        except KeyError:
            return Response({'message': self.error_message, 'status': status.HTTP_403_FORBIDDEN})


class LogoutView(ViewSet):
    message = 'You have successfully logged out'

    def retrieve(self, request):
        logout(request)
        return Response({'message': self.message, 'status': status.HTTP_200_OK})


class TokenView(TokenObtainPairView):
    serializer_class = TokenSerializer


class ProfileListView(ViewSet):
    model = Profile.objects.all()
    permission_classes = [IsAuthenticated, IsSuperUser]
    authentication_classes = [JWTAuthentication]

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

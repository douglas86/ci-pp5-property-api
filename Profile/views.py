from django.shortcuts import render
from adrf.viewsets import ViewSet
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.admin import User

from Profile.models import Profile


# Create your views here.
class ProfileView(APIView):
    """
    This view is used for displaying profile information
    """

    model = Profile
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = [user for user in self.model.objects.filter(user=request.user)]
        return Response(user)

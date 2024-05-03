from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.admin import User

from .models import Profile
from .serializers import ProfileSerializer


# Create your views here.
class ProfileList(APIView):
    """
    This view is used for displaying profile information
    """

    model = Profile

    def get(self, request):
        profile = self.model.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)

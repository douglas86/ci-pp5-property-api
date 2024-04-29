from django.shortcuts import render
from adrf.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authtoken.admin import User

from Profile.models import Profile


# Create your views here.
class ProfileView(ViewSet):
    model = Profile
    message = 'Hello, World!'

    async def list(self, request):
        return Response({'message': self.message})

    async def retrieve(self, request):
        user = await self.model.objects.all()
        return Response({'user': user})
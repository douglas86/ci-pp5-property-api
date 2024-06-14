import asyncio

from adrf.viewsets import ViewSet
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from Profile.models import Profile
from Profile.serializers import ProfileSerializer


class HomeView(ViewSet):
    username = ""
    password = ""
    message = 'This is the home view'

    async def list(self, request):
        return Response({'message': self.message})


class AsyncViewSet:

    def __init__(self, model, **kwargs):
        super().__init__(**kwargs)
        self.model = model

    async def async_generator(self):
        yield self.model

    async def async_coroutine(self):
        async for data in self.async_generator():
            return data

    async def get_queryset(self):
        task = asyncio.create_task(self.async_coroutine())
        return await task

    def main(self):
        data = asyncio.run(self.get_queryset())
        return data

    def retrieve(self):
        data = self.main()
        return data


class LoginView(ViewSet):
    model = Profile.objects.all()
    username = None
    password = None
    pk = None
    message = 'You have successfully logged in'
    error_message = 'The credentials entered are incorrect.'

    def get_profile(self):
        profile_model = self.model
        profile = AsyncViewSet(profile_model).retrieve()
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

import asyncio

from adrf.viewsets import ViewSet
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response


class HomeView(ViewSet):
    username = ""
    password = ""
    message = 'This is the home view'

    async def list(self, request):
        return Response({'message': self.message})


class LoginView(ViewSet):
    model = User.objects.all().values('id', 'username', 'password')
    username = None
    password = None
    message = 'You have successfully logged in'
    error_message = 'The credentials entered are incorrect.'

    async def async_generator(self):
        user = self.model
        yield user

    async def async_coroutine(self):
        async for user in self.async_generator():
            return user

    async def main(self):
        task = asyncio.create_task(self.async_coroutine())
        return await task

    def search(self):
        data = asyncio.run(self.main())
        return [element for element in data if element['username'] == self.username]

    def checks(self):
        user = authenticate(username=self.username, password=self.password)

        if user is None:
            return {'message': self.error_message, 'status': status.HTTP_404_NOT_FOUND}
        else:
            return {'message': self.message, 'status': status.HTTP_200_OK, 'user': self.search()}

    def retrieve(self, request):
        self.username = request.POST['username']
        self.password = request.POST['password']

        return Response(self.checks())

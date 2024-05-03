from django.contrib.auth.models import User
from django.test import TestCase, Client


# Create your tests here.
class TestUser(TestCase):
    """
    Test if user can register, login, logout and change password
    """

    def setUp(self):
        """
        Set up the client for the test database
        :return:
        """

        self.client = Client()

    def register_user(self):
        """
        Register user
        :return:
        """

        response = self.client.post('/dj-rest-auth/registration/',
                                    {'username': 'test', 'password1': 'IAMininGLOrN', 'password2': 'IAMininGLOrN'})
        return response

    def login_user(self):
        """
        Login user
        :return:
        """

        self.register_user()
        user = self.client.post('/dj-rest-auth/login/', {'username': 'test', 'password': 'IAMininGLOrN'})
        return user

    def test_register(self):
        """
        Test if user can register user
        Check if http status code is 201
        Meaning that the resources returned generated an access token and refresh token
        :return:
        """

        response = self.register_user()
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        """
        Test if user can log in
        Check if http status code is 200
        :return:
        """

        user = self.login_user()
        self.assertEqual(user.status_code, 200)

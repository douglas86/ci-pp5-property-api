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

    def test_register(self):
        """
        Test if user can register user
        Check if http status code is 201
        Meaning that the resources returned generated an access token and refresh token
        :return:
        """

        response = self.client.post('/dj-rest-auth/registration/',
                                    {'username': 'test', 'password1': 'IAMininGLOrN', 'password2': 'IAMininGLOrN'})
        self.assertEqual(response.status_code, 201)

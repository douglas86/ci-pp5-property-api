from django.test import TestCase, Client
from Profile.tests import TestUser


# Create your tests here.
class TestStocks(TestCase):
    """
    Test if only the admin can create a Property on the site
    """

    def setUp(self):
        """
        Set up the client for the test database
        :return:
        """

        self.client = Client()

    def register_user(self):
        """
        Register a new user with a role as user
        :return:
        """

        response = self.client.post('/dj-rest-auth/registration/',
                                    {'username': 'test', 'password1': 'IAMininGLOrN', 'password2': 'IAMininGLOrN',
                                     'role': 'user'})

        return response

    def login_user(self):
        self.register_user()
        user = self.client.post('/dj-rest-auth/login/', {'username': 'test', 'password': 'IAMininGLOrN'})
        return user

    def test_create_property(self):
        """
        Testing if I can create a Property
        :return:
        """

        response = self.register_user()
        self.assertEqual(response.status_code, 201)

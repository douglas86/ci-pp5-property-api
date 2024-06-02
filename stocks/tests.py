import io

from django.contrib.auth.models import User
from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from Profile.tests import TestUser
from .models import Stocks
import io
from PIL import Image


def get_temporary_image():
    """
    Creates a temporary image and returns it.
    :return:
    """
    image = Image.new('RGB', (100, 100))
    temp_image = io.BytesIO()
    image.save(temp_image, format='JPEG')
    temp_image.seek(0)
    return temp_image


# Create your tests here.
class TestStocks(APITestCase):
    """
    Test if only the admin can create a Property on the site
    """

    def setUp(self):
        """
        create new users for testing
        :return:
        """

        # create admin and user
        self.admin_user = User.objects.create_superuser(username='admin', password='IAMininGLOrN')
        self.regular_user = User.objects.create_user(username='user', password='IAMininGLOrN')
        self.url = '/stocks/create/'

    def posting_data(self):
        temp_image = get_temporary_image()
        image_file = SimpleUploadedFile("temp_image.jpg", temp_image.read(), content_type="image/jpeg")

        data = {
            "owner": self.admin_user.id,
            "property_image": image_file,
            "property_address": "7 - 11 High Street, Reigate",
            "property_area": "Reigate",
            "area_code": "RH29AA",
            "rent": 700,
            "created_at": "2024-02-15T13:20:30+03:00",
            "updated_at": "2024-02-15T13:20:30+03:00"
        }

        return data

    def test_cannot_create_property(self):
        """
        Test that if you are not logged in, you cannot create a property
        :return:
        """

        response = self.client.post(self.url, data=self.posting_data(), format='multipart')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_not_admin(self):
        """
        Test that if you are logged in and not the admin,
        You cannot create a property
        :return:
        """

        self.client.login(username='user', password='IAMininGLOrN')

        response = self.client.post(self.url, data=self.posting_data(), format='multipart')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_in_user_can_create_property(self):
        """
        Test if a user can create a Property
        :return:
        """
        self.client.login(username='admin', password='IAMininGLOrN')

        temp_image = get_temporary_image()
        image_file = SimpleUploadedFile("temp_image.jpg", temp_image.read(), content_type="image/jpeg")

        url = '/stocks/create/'

        data = {
            "owner": self.admin_user.id,
            "property_image": image_file,
            "property_address": "7 - 11 High Street, Reigate",
            "property_area": "Reigate",
            "area_code": "RH29AA",
            "rent": 700,
            "created_at": "2024-02-15T13:20:30+03:00",
            "updated_at": "2024-02-15T13:20:30+03:00"
        }

        response = self.client.post(url, data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Stocks.objects.count(), 1)
        self.assertEqual(Stocks.objects.get().owner, self.admin_user)

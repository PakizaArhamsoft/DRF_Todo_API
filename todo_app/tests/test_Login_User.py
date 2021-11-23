"""
   Testing the Login User API
"""
import pytest
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


@pytest.mark.django_db
class LoginUserTestCase(APITestCase):
    """
    Test login api with valid and invalid credentials.
    """

    def setUp(self) -> None:
        User.objects.create_user(
            first_name='test',
            last_name='test',
            email='test@gmail.com',
            username='test',
            password='test123456'
        )

    def test_login_user(self):
        """
        test the login api with +ive and -ive cases
        """

        url = '/api/login/'
        data1 = {
            'username': 'test',
            'password': 'test123456'
        }
        response1 = self.client.post(url, data1)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)

        data2 = {
            'username': 'test',
            'password': 'test'
        }
        response2 = self.client.post(url, data2)
        self.assertEqual(response2.status_code, status.HTTP_401_UNAUTHORIZED)

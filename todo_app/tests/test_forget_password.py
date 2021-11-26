"""
   Testing Reset Password API
"""

import pytest
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


@pytest.mark.django_db
class ForgotPasswordTestCase(APITestCase):
    """
    Test Forgot Password api
    """
    def setUp(self) -> None:
        User.objects.create_user(
            first_name='test',
            last_name='test',
            email='test@gmail.com',
            username='test',
            password='test1234'
        )
        self.url = '/api/password_reset/'

    def test_forgot_password_valid(self):
        """
        change the password with basic authentication
        and generate token to update password
        """

        data1 = {
            "email": "test@gmail.com"
        }
        response1 = self.client.post(self.url, data1)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)

    def test_forgot_password_invalid(self):
        """
        change the password with basic authentication
        and generate token to update password
        """
        data2 = {
            "email": "pakiza@gmail.com"
        }
        response2 = self.client.post(self.url, data2)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

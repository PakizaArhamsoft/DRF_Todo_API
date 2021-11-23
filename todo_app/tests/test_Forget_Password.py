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

    def test_forgot_password(self):
        """
        change the password with basic authentication
        and generate token to update password
        """
        User.objects.create_user(
            first_name='test',
            last_name='test',
            email='test@gmail.com',
            username='test',
            password='test1234'
        )
        url = '/api/password_reset/'
        data1 = {
            "email": "test@gmail.com"
        }
        data2 = {
            "email": "pakiza@gmail.com"
        }
        response1 = self.client.post(url, data1)
        response2 = self.client.post(url, data2)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

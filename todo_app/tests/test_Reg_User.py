"""
   Testing the Register new User API
"""
import pytest
from rest_framework import status
from rest_framework.test import APITestCase


@pytest.mark.django_db
class RegistrationTestCase(APITestCase):
    """
    Test User Registration In different cases.
    """

    def test_registration(self):
        """
            Test the Reg api with valid and
            invalid credentials.
        """

        data = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test_user@test.com',
            'username': 'test_user',
            'password': 'Test_user_password_123',
        }
        data1 = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test_user@test.com',
            'username': 'test_user',
            'password': '123',
        }

        url = '/reg/'
        response1 = self.client.post(url, data)
        response2 = self.client.post(url, data)  # duplicate user
        response3 = self.client.post(url, data1)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response3.status_code, status.HTTP_400_BAD_REQUEST)

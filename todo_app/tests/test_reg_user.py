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
    def setUp(self) -> None:
        self.url = '/reg/'

    def test_registration_valid(self):
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
        response1 = self.client.post(self.url, data)
        response2 = self.client.post(self.url, data)  # duplicate user
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_invalid(self):
        """
            Test the Reg api with valid and
            invalid credentials.
        """
        data1 = {
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test_user@.com',
            'username': 'test_user',
            'password': '123',
        }
        response3 = self.client.post(self.url, data1)
        self.assertEqual(response3.status_code, status.HTTP_400_BAD_REQUEST)

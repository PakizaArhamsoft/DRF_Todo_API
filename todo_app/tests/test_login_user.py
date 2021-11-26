"""
   Testing the Login User API

"""

from .test_base_api import pytest, User, APITestCase, status


@pytest.mark.django_db
class LoginUserTestCase(APITestCase):
    """
    Test login api with valid and invalid credentials.
    """

    def setUp(self) -> None:
        User.objects.create_user(
            first_name='pakiza',
            last_name='ehsan',
            email='pakii@gmail.com',
            username='test',
            password='test123456'
        )
        self.url = '/api/login/'

    def test_login_valid_user(self):
        """
        test the login api with +ive and -ive cases
        """
        data1 = {
            'username': 'test',
            'password': 'test123456'
        }
        response1 = self.client.post(self.url, data1)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)

    def test_login_invalid_user(self):
        """
        test the login api with -ive cases
        """
        data2 = {
            'username': 'test',
            'password': 'test'
        }
        response2 = self.client.post(self.url, data2)
        self.assertEqual(response2.status_code, status.HTTP_401_UNAUTHORIZED)

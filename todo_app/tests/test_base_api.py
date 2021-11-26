"""
Base class for User Auth Setup
"""
import pytest
from rest_framework import status
from rest_framework.test import APITestCase
from todo_app.models import User, Position, Employee


@pytest.mark.django_db
class BaseTest(APITestCase):
    """
    Base class used for CRUD API
    """
    def setUp(self) -> None:
        """
                Setup required things for employee creating i.e user.
        """
        self.user = User.objects.create_user(
            first_name='test',
            last_name='test',
            email='pakiza@test.com',
            username='pakiza',
            password='pakiza1234'
        )
        self.url = '/api/login/'
        resp = self.client.post(
            self.url,
            {'username': 'pakiza', 'password': 'pakiza1234'},
            format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in resp.data)
        token = resp.data['access']

        self.headers = {
            'accept': 'application/json',
            'HTTP_AUTHORIZATION': f'Bearer {token}',
        }

        self.positions = Position.objects.create(   # pylint: disable=E1101
            title='Python Developer')
        self.positions.save()
        self.task = Employee.objects.create(
            user=self.user,
            emp_name='fds',
            emp_code=2,
            mobile='+12125552383',
            position=self.positions)
        self.task.save()

    def Login_Invalid(self):  # pylint: disable=C0103
        """
        Login the user with invalid credentials
        """
        data = {
            'username': 'pakii',
            'password': 'pakiza'
        }
        resp = self.client.post(
            self.url,
            data,
            format='json')
        self.user = data['username']
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
        # self.assertFalse('access' in resp.data)
        # token = resp.data['access']
        #
        # self.headers = {
        #     'accept': 'application/json',
        #     'HTTP_AUTHORIZATION': f'Bearer {token}',
        # }

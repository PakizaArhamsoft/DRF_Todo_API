"""
   Testing Employee CRUD API
"""

import pytest
from rest_framework import status
from rest_framework.test import APITestCase
from todo_app.models import User, Position, Employee


@pytest.mark.django_db
class TaskTestCase(APITestCase):
    """
    Test Employee Creation API
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
        self.user.save()

        url = '/api/login/'
        resp = self.client.post(
            url,
            {'username': 'pakiza', 'password': 'pakiza1234'},
            format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in resp.data)
        token = resp.data['access']

        self.headers = {
            'accept': 'application/json',
            'HTTP_AUTHORIZATION': f'Bearer {token}',
        }

        self.positions = Position.objects.create(
            title='Python Developer')
        self.positions.save()
        # positions = Position.objects.create(
        #     title='PHP Developer')
        # positions.save()
        self.task = Employee.objects.create(
            user=self.user,
            emp_name='fds',
            emp_code=2,
            mobile='+12125552383',
            position=self.positions)
        self.task.save()

    def test_create_task(self):
        """
        #         Employees create.
        #         """
        # positions = Position.objects.create(
        #     title='Python Developer')
        # positions.save()
        #
        # task = Employee.objects.create(
        #     user=self.user,
        #     emp_name='example',
        #     emp_code=3,
        #     mobile='+12125552380',
        #     position=positions)
        # task.save()
        data1 = {
            # "user": self.user.id,
            "emp_name": "fds",
            "mobile": "+12125552389",
            "emp_code": 1,
            "position": self.positions.id
        }
        # Invalid data
        data2 = {
            "emp_name": "",  # empty field
            "mobile": "+1212555238956",  # invalid phone number
            "emp_code": 1,
            "position": self.positions.id
        }
        url = '/employee-view/'
        response1 = self.client.post(path=url, data=data1, **self.headers)
        response2 = self.client.post(path=url, data=data2, **self.headers)

        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_list(self):
        """
        #         Employees complete list retrieve.
        #         """
        db_task = Employee.objects.all()
        print(db_task)
        # profile_list = Employee.objects.get_queryset().order_by('id')
        # paginator = Paginator(profile_list, 1)
        url = f'/employee-view/'
        print(url)
        req = self.client.get(url, **self.headers)

        self.assertEqual(req.status_code, status.HTTP_200_OK)

    def test_task_retrieve(self):
        """
               Tasks retrieve
        """
        db_task = Employee.objects.filter(user=self.user).first()
        db_project = User.objects.filter(username=self.user).first()
        print(db_task, db_project)
        url = f'/employee-view/{db_task.id}/'
        print(url)
        req = self.client.get(url, **self.headers)

        self.assertEqual(req.status_code, status.HTTP_200_OK)

    def test_task_update(self):
        """
        #         Tasks update.
        #         """

        db_task = Employee.objects.filter(user=self.user).first()

        data1 = {
            # "user": self.user.id,
            "emp_name": "fds",
            "mobile": "+12125552356",
            "emp_code": 7,
            "position": self.positions.id
        }
        # invalid data and incomplete data
        data2 = {
            "emp_name": "fds",
            "mobile": "+121255523563",
            "position": self.positions.id
        }
        url = f'/employee-view/{db_task.id}/'
        print(url)
        response1 = self.client.put(url, data1, **self.headers)
        response2 = self.client.put(url, data2, **self.headers)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_task_patch(self):
        """
        #         Tasks partial update.
        #         """
        #
        db_task = Employee.objects.filter(user=self.user).first()

        data1 = {

            "mobile": "+12125552350",
            "emp_code": 9,

        }
        # invalid data
        data2 = {
            "emp_name": "",
            "mobile": "+1212555235639",
            "emp_code": -1,
        }
        url = f'/employee-view/{db_task.id}/'
        print(url)

        url = f'/employee-view/{db_task.id}/'
        response1 = self.client.patch(url, data1, **self.headers)
        response2 = self.client.put(url, data2, **self.headers)

        self.assertEqual(response1.status_code, status.HTTP_200_OK)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_task_delete(self):
        """
        #         Tasks delete.
        #         """
        #
        db_task = Employee.objects.filter(user=self.user).first()

        url = f'/employee-view/{db_task.id}/'
        print(url)
        req = self.client.delete(url, **self.headers)

        self.assertEqual(req.status_code, status.HTTP_204_NO_CONTENT)

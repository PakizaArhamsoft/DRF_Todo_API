"""
   Testing Employee CRUD API
"""
from .test_base_api import pytest, status, Employee, BaseTest


@pytest.mark.django_db
class TaskTestCase(BaseTest):
    """
    Test Employee Creation API
    """

    def setup(self) -> None:
        """
        Setup required things for employee creating i.e user.
        """
        super(self.__class__, self).setUp()  # pylint: disable=E1003

    def test_create_task_valid_data(self):
        """
        #         Employees create.
        #         """
        data1 = {
            "emp_name": "fds",
            "mobile": "+12125552389",
            "emp_code": 1,
            "position": self.positions.id
        }
        url = '/employee-view/'
        response1 = self.client.post(path=url, data=data1, **self.headers)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)

    def test_create_task_invalid_data(self):
        """
        #         Employees create with Invalid data.
        #         """
        data2 = {
            "emp_name": "",  # empty field
            "mobile": "+1212555238956",  # invalid phone number
            "emp_code": 1,
            "position": self.positions.id
        }
        url = '/employee-view/'
        response2 = self.client.post(path=url, data=data2, **self.headers)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_task_invalid_user(self):
        """
        #         Employees create with Invalid User.
        #         """
        data2 = {
            "emp_name": "",  # empty field
            "mobile": "+1212555238956",  # invalid phone number
            "emp_code": 1,
            "position": self.positions.id
        }
        url = '/employee-view/'
        response2 = self.client.post(path=url, data=data2)
        self.assertEqual(response2.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list_valid_credentials(self):
        """
        #         Employees complete list retrieve.
        #         """
        Employee.objects.all()
        url = '/employee-view/'
        req = self.client.get(url, **self.headers)
        self.assertEqual(req.status_code, status.HTTP_200_OK)

    def test_get_list_invalid_user(self):
        """
        #         Employees complete list retrieve.
        #         """
        self.Login_Invalid()
        Employee.objects.all()
        url = '/employee-view/'
        req = self.client.get(url)
        self.assertEqual(req.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_task_retrieve_valid(self):
        """
               Tasks retrieve
        """
        db_task = Employee.objects.filter(user=self.user).first()
        url = f'/employee-view/{db_task.id}/'
        req = self.client.get(url, **self.headers)

        self.assertEqual(req.status_code, status.HTTP_200_OK)

    def test_task_retrieve_invalid(self):
        """
               Tasks retrieve
        """
        self.Login_Invalid()
        url = f'/employee-view/{1}/'
        req = self.client.get(url)
        self.assertEqual(req.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_task_retrieve_notExist(self):   # pylint: disable=C0103
        """
               Tasks retrieve
        """
        Employee.objects.filter(user=self.user).first()
        url = f'/employee-view/{1000}/'
        req = self.client.get(url, **self.headers)
        self.assertEqual(req.status_code, status.HTTP_404_NOT_FOUND)

    def test_task_valid_update(self):
        """
        #         Tasks update.
        #         """
        db_task = Employee.objects.filter(user=self.user).first()
        data1 = {
            "emp_name": "fds",
            "mobile": "+12125552356",
            "emp_code": 7,
            "position": self.positions.id
        }
        url = f'/employee-view/{db_task.id}/'
        response1 = self.client.put(url, data1, **self.headers)
        self.assertEqual(response1.data['user_id'], db_task.user_id)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)

    def test_task_invalid_update(self):
        """
        #         Tasks update with Invalid data.
        #         """

        db_task = Employee.objects.filter(user=self.user).first()
        data2 = {
            "emp_name": "fds",
            "mobile": "+121255523563",
            "position": self.positions.id
        }
        url = f'/employee-view/{db_task.id}/'
        response2 = self.client.put(url, data2, **self.headers)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_task_update_notExist(self):   # pylint: disable=C0103
        """
         Tasks update with Invalid data.
        """
        Employee.objects.filter(user=self.user).first()
        data2 = {
            "emp_name": "fds",
            "mobile": "+121255523563",
            "position": self.positions.id
        }
        url = f'/employee-view/{10000}/'
        response2 = self.client.put(url, data2, **self.headers)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)

    def test_task_update_invalid_user(self):
        """
        #         Tasks update.
        #         """
        self.Login_Invalid()
        data1 = {
            "emp_name": "fds",
            "mobile": "+12125552356",
            "emp_code": 7,
            "position": self.positions.id
        }
        url = f'/employee-view/{1}/'
        response1 = self.client.put(url, data1)
        self.assertEqual(response1.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_task_valid_patch(self):
        """
        #         Tasks partial update.
        #         """
        #
        db_task = Employee.objects.filter(user=self.user).first()
        data1 = {
            "mobile": "+12125552350",
            "emp_code": 9,
        }
        url = f'/employee-view/{db_task.id}/'
        response1 = self.client.patch(url, data1, **self.headers)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)

    def test_task_invalid_patch(self):
        """
        #         Tasks partial update.
        #         """
        db_task = Employee.objects.filter(user=self.user).first()
        data2 = {
            "emp_name": "",
            "mobile": "+1212555235639",
            "emp_code": -1,
        }
        url = f'/employee-view/{db_task.id}/'
        response2 = self.client.put(url, data2, **self.headers)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_task_patch_notExist(self):  # pylint: disable=C0103
        """
         Tasks update with Invalid data.
        """
        Employee.objects.filter(user=self.user).first()
        data2 = {
            "emp_name": "fds",
            "mobile": "+121255523563",
        }
        url = f'/employee-view/{10000}/'
        response2 = self.client.put(url, data2, **self.headers)
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)

    def test_task_patch_invalid_user(self):
        """
        #         Tasks update.
        #         """
        self.Login_Invalid()
        data1 = {
            "emp_name": "fds",
            "emp_code": 7,
        }
        url = f'/employee-view/{1}/'
        response1 = self.client.put(url, data1)
        self.assertEqual(response1.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_task_delete(self):
        """
        #         Tasks delete.
        #         """
        #
        db_task = Employee.objects.filter(user=self.user).first()
        url = f'/employee-view/{db_task.id}/'
        req = self.client.delete(url, **self.headers)
        self.assertEqual(req.status_code, status.HTTP_204_NO_CONTENT)

    def test_task_delete_notExist(self):  # pylint: disable=C0103
        """
        #         Tasks delete.
        #         """
        Employee.objects.filter(user=self.user).first()
        url = f'/employee-view/{1000}/'
        req = self.client.delete(url, **self.headers)
        self.assertEqual(req.status_code, status.HTTP_404_NOT_FOUND)

    def test_task_delete_invalid_user(self):
        """
        #         Tasks delete.
        #         """
        self.Login_Invalid()
        url = f'/employee-view/{1}/'
        req = self.client.delete(url)
        self.assertEqual(req.status_code, status.HTTP_401_UNAUTHORIZED)

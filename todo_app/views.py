"""
   views.py create the views of app

"""
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import AdminRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.backends import TokenBackend

from .models import Employee
from .serializers import EmployeeSerializer, RegisterSerializer


class RegUserView(CreateAPIView):
    """
    Register the User
    """
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer, AdminRenderer]
    serializer_class = RegisterSerializer


class EmployeeViewSet(ModelViewSet):
    """
    Employee create, get list of Employees w.r.t User, update,
    delete and retrieve specific Employee data
    """
    model = Employee
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):

        token = self.request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
        user = valid_data['user_id']

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(pk=user)
        serializer.validated_data['user'] = user
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        token = self.request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
        tasks = Employee.objects.filter(user=valid_data['user_id'])   # filter by User
        self.queryset = tasks
        return tasks

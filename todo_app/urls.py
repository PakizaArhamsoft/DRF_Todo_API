"""
  URL paths of todo_app
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

APP_NAME = "todo_app"

ROUTER = DefaultRouter()
ROUTER.register(r'employee-view', views.EmployeeViewSet, basename='employee')

urlpatterns = [  # pylint: disable=C0103
    path('', include(ROUTER.urls)),
    path('reg/', views.RegUserView.as_view(), name='register'),
]

""""
 Serialize(translate) the Model objects into understandable data types
"""
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Position, Employee


class RegisterSerializer(serializers.ModelSerializer):
    """
    Create new User Model Serializer
    """
    class Meta:
        """
            fields behaviour inner Model class
        """
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        extra_kwargs = {'password': {'style': {'input_type': 'password'}}}

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.is_staff = True
        user.save()
        return user


class PositionSerializer(serializers.ModelSerializer):
    """
        Create Position Model Serializer
    """
    class Meta:
        """
            fields behaviour inner Model class
        """
        model = Position
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Create Employee Model Serializer
    """
    class Meta:
        """
        fields behaviour inner Model class
        """
        model = Employee
        fields = ['id', 'emp_name', 'mobile', 'emp_code', 'position', 'user_id']

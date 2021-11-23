"""
 Register the Models
"""
from django.contrib import admin
from .models import Employee, Position

admin.site.register(Position)
admin.site.register(Employee)

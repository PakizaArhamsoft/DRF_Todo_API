"""
 app configuration
"""
from django.apps import AppConfig


class TodoAppConfig(AppConfig):
    """
    todo_App configuration
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo_app'

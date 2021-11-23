"""
  Create DB collections of our API
"""
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from softdelete.models import SoftDeleteObject

from phonenumber_field.modelfields import PhoneNumberField


class Position(models.Model):
    """
        Position of Employee Model Class
    """
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)


class Employee(SoftDeleteObject, models.Model):
    """
    Employee Credentials Model Class
    """
    user = models.ForeignKey(User, null=True, related_name='parent_user', on_delete=models.SET_NULL)
    emp_name = models.CharField(max_length=200, null=False, blank=False)
    mobile = PhoneNumberField(blank=False, default="+12125552369", unique=True)
    emp_code = models.IntegerField(null=False, blank=False, default=0, unique=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=False)
    indexes = [models.Index(fields=['title'])]

    def __str__(self):
        data = str(self.emp_name) + " ______ " + str(self.position)
        return data


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Token Created for Reset Password
    """

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'),
                                                   reset_password_token.key)
    print(sender, instance, args, kwargs)
    send_mail(
        # title:
        "Password Reset for {title}".format(title="Reset Password!!"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )

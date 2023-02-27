from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.conf import settings

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    # phoneNumberRegex = RegexValidator(regex=r'^(\+375)(29|25|44|33)(\d{7})$)')
    # phone_number = models.CharField('phone_number', validators=[phoneNumberRegex], max_length=13, unique=True)
    phone_number = models.CharField('phone_number', max_length=13, unique=True)
    username = models.CharField('username', max_length=255, null=True, blank=True, unique=True)
    email = models.EmailField('email', null=True, blank=True)
    date_joined = models.DateTimeField('date_joined', auto_now_add=True)
    is_active = models.BooleanField('is_active', default=False)
    is_staff = models.BooleanField('is_staff', default=False)
    is_verified = models.BooleanField('is_verified', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

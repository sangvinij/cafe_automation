import uuid

from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
# from django.conf import settings

from .managers import UserManager
from management.models import Menu


class User(AbstractBaseUser, PermissionsMixin):
    phoneNumberRegex = RegexValidator(regex=r'^(\+375)(29|25|44|33)(\d{7})$')
    phone_number = models.CharField('phone_number', validators=[phoneNumberRegex], max_length=13, unique=True)
    # phone_number = models.CharField('phone_number', max_length=13, unique=True)
    first_name = models.CharField('first_name', max_length=255, null=True, blank=True)
    last_name = models.CharField('last_name', max_length=255, null=True, blank=True)
    email = models.EmailField('email', null=True, blank=True)
    is_active = models.BooleanField('is_active', default=True)
    is_staff = models.BooleanField('is_staff', default=False)
    is_verified = models.BooleanField('is_verified', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.first_name:
            return self.first_name
        return self.phone_number

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          editable=False,
                          primary_key=True,
                          unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class CartItems(models.Model):
    cart = models.ForeignKey(Cart,
                             on_delete=models.CASCADE,
                             related_name='carts',
                             null=True,
                             blank=True)
    item = models.ForeignKey(Menu,
                             on_delete=models.CASCADE,
                             related_name='items',
                             null=True,
                             blank=True)
    amount = models.IntegerField(default=0)

import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models


from management.models import CafeAddresses, Menu

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    phoneNumberRegex = RegexValidator(regex=r'^(\+375)(29|25|44|33)(\d{7})$')
    phone_number = models.CharField('phone_number', validators=[phoneNumberRegex], max_length=13, unique=True)
    first_name = models.CharField('first_name', max_length=255, null=True, blank=True)
    last_name = models.CharField('last_name', max_length=255, null=True, blank=True)
    email = models.EmailField('email', null=True, blank=True)
    is_active = models.BooleanField('is_active', default=True)
    is_staff = models.BooleanField('is_staff', default=False)
    is_verified = models.BooleanField('is_verified', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

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

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


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
    amount = models.PositiveSmallIntegerField(default=1)

    class Meta:
        verbose_name = 'Объект корзины'
        verbose_name_plural = 'Объекты корзины'


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey('OrderStatus', on_delete=models.SET_NULL, null=True)
    cafe_address = models.ForeignKey(CafeAddresses, on_delete=models.CASCADE)
    commentary = models.TextField(max_length=1000, null=True, blank=True)
    payment_type = models.ForeignKey('PaymentType', on_delete=models.SET_DEFAULT, default='Наличные')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderStatus(models.Model):
    status_name = models.CharField(max_length=255)

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class PaymentType(models.Model):
    payment_type = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.payment_type

    class Meta:
        verbose_name = 'Способ оплаты'
        verbose_name_plural = 'Способы оплаты'

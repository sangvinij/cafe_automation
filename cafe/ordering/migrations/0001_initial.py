# Generated by Django 4.1.7 on 2023-03-04 16:10

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import ordering.managers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '__first__'),
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('phone_number', models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(regex='^(\\+375)(29|25|44|33)(\\d{7})$')], verbose_name='phone_number')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='first_name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='last_name')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is_staff')),
                ('is_verified', models.BooleanField(default=False, verbose_name='is_verified')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
            },
            managers=[
                ('objects', ordering.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='ordering.cart')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='management.menu')),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-02-27 17:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0003_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(regex='^(\\+375)(29|25|44|33)(\\d{7})$)')], verbose_name='phone_number'),
        ),
    ]
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number=None, username=None,
                     password=None, **extra_fields):

        if not username:
            if not phone_number:
                raise ValueError('The phone number must be set')

        if phone_number:
            if not username:
                username = phone_number

        user = self.model(
            username=username,
            phone_number=phone_number,
            **extra_fields
        )

        if extra_fields.get('is_superuser'):
            user = self.model(
                username=username,
                **extra_fields
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(phone_number=phone_number, username=username, password=password, **extra_fields)

    def create_superuser(self, phone_number, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(
            phone_number=phone_number,
            username=username,
            password=password,
            **extra_fields
        )

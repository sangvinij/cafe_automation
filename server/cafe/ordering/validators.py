import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class PassValidator(object):
    password_regex = re.compile('^(?=.*?[a-z])(?=.*?[0-9]).{5,}$')

    def validate(self, password, user=None):
        if not self.password_regex.fullmatch(password):
            raise ValidationError(
                _('Минимум 5 символов, 1 латинская буква и 1 цифра'),
                code='wrong password',
            )

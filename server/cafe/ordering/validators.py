import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class PassValidator(object):
    password_regex = re.compile('^(?=.*?[a-z])(?=.*?[0-9]).{5,}$')

    def validate(self, password, user=None):
        if not self.password_regex.fullmatch(password):
            raise ValidationError(
                _('TThe password must contain at least one letter, '
                  'one digit and must be more then 5 characters'),
                code='wrong password',
            )

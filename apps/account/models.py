from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db.models import (
    EmailField,
)
from django.utils.translation import gettext_lazy as _

from apps.account.managers import AccountManager

from rest_framework_simplejwt.tokens import RefreshToken


class Account(AbstractUser):
    email = EmailField(unique=True)
    USERNAME_FIELD = "email"
    objects = AccountManager()
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")
        db_table = "account"

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        ts = refresh.access_token.payload['exp']
        dt = datetime.fromtimestamp(ts)
        data = {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'expires_in': str(dt),
            'account_id': str(self.id),
        }
        return data

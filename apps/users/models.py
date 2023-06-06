from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(_("phone number"), max_length=20, unique=True)
    password = models.CharField(_("password"), max_length=128)
    full_name = models.CharField(_("full name"), max_length=50, blank=True)
    extra_data = models.JSONField(_("extra data"), default=dict, blank=True)
    is_staff = models.BooleanField(_("is staff"), default=False)
    is_superuser = models.BooleanField(_("superuser status"), default=False)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    last_login = models.DateTimeField(_("last login"), blank=True, null=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["full_name"]

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.full_name or self.phone_number

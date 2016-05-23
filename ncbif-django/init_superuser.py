# coding: utf-8

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

DEFAULT_ADMIN_USERNAME = "ncbif_admin"
DEFAULT_ADMIN_EMAIL = "ncbif_admin@ncbif.nc"
DEFAULT_ADMIN_PASSWORD = "ncbif"

try:
    User.objects.get(username=DEFAULT_ADMIN_USERNAME)
except ObjectDoesNotExist:
    User.objects.create_superuser(
        DEFAULT_ADMIN_USERNAME,
        DEFAULT_ADMIN_EMAIL,
        DEFAULT_ADMIN_PASSWORD
    )


from django.contrib.auth.models import AbstractUser
from django.db import models
from products.models import VolunteerOrganization


class CustomUser(AbstractUser):
    organization = models.ForeignKey(
        VolunteerOrganization, null=True, blank=True, on_delete=models.SET_NULL
    )

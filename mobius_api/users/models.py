from __future__ import unicode_literals

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
# from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    national_id = models.CharField(max_length=15, blank=True, null=False)
    phone = models.CharField(max_length=12, default='')
    email = models.EmailField()

    def __str__(self):
        return self.username


class Info(models.Model):
    '''
    Internal User table
    '''
    email = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.email

from django.db import models
from django.contrib.auth.models import (AbstractBaseUser)


class Site_User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    dob = models.DateField()
    password = models.CharField(max_length=30, blank=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_notified = models.BooleanField(default=False)

    # objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['dob', 'email']

    def __str__(self):
        return self.email



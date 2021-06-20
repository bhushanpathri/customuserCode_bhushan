from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from. managers import *
# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=10, unique=True)
    is_email_verify = models.BooleanField(default='False')

    status = models.BooleanField(default='False')

    object = UserManager()

    USERNAME_FIELD = 'mobile_no'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

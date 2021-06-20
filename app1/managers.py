from django.contrib.auth.base_user import BaseUserManager

from.models import *
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, mobile_no, password=None, **extra_fields):
        if not mobile_no:
            raise ValueError('mobile number is required')
        user = self.model(mobile_no=mobile_no, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_no, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(mobile_no, password, **extra_fields)

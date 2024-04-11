from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager

# Create your User Model here.
class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(db_index=True, unique=True, blank=False, max_length=100)
    is_staff = models.BooleanField('staff',default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'


    @property
    def is_authenticated(self):
        """
        Allways returns True
        :return: True
        """
        return True

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
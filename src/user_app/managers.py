
from django.contrib.auth.models import BaseUserManager

# Create your CustomUserManager here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, password, username, **extra_fields):
        if not username:
            raise ValueError("Username must be provided")
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
            username = username,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, password, username, **extra_fields):
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(password, username, **extra_fields)

    def create_superuser(self, password, username, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(password, username, **extra_fields)
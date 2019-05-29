from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, password=None):
        if username is None or password is None:
            raise ValueError('User must have a username and a password.')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, unique=True, max_length=16)
    status = models.CharField(max_length=134, blank=True)
    about = models.TextField(blank=True)
    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return self.username

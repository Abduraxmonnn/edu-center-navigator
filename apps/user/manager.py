# Django
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.manager import BaseManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager, BaseManager):
    def create_user(self, email, password):
        """
        Creates and saves a User with the given username, date of
        birth and password.
        """
        if not email:
            raise ValueError(_('Users must have an email address'))
        if not password:
            raise ValueError(_('Users must have an password'))

        user = self.model(email=email.strip(), )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_admin(self, email, password):
        """
        Creates and saves an admin with the given username and password.
        """
        user = self.create_user(email, password)
        user.is_registered = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given username, date of
        birth and password.
        """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.is_registered = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

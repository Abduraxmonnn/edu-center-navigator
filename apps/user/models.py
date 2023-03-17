# Django
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxValueValidator
from django.db import models

# Project
from apps.user.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    This is User model that can be admin or just user of certain center.
    We give permissions leave the Users status (ex: Admin, User of Center...)
    Every User's username have to unique.
    Every User privileges begin as default User, not stuff, admin, superuser
    """
    name = models.CharField(
        max_length=150
    )
    surname = models.CharField(
        max_length=150
    )
    dob = models.DateField(
        blank=True,
        null=True
    )
    username = models.CharField(
        max_length=255
    )
    phone_number = models.CharField(
        max_length=13,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        unique=True
    )
    # Time should be given in minutes (10 sec = 0.16 min)
    spend_time = models.FloatField(
        blank=True,
        null=True
    )
    send_news = models.BooleanField(
        default=False
    )

    # Verify email fields
    is_verified = models.BooleanField(
        default=False
    )
    otp = models.CharField(
        max_length=6,
        blank=True,
        null=True
    )
    expires_at = models.DateTimeField(
        null=True
    )

    is_admin = models.BooleanField(
        default=False
    )
    is_superuser = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=True
    )

    last_login = models.DateTimeField(
        blank=True,
        null=True
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    last_updated = models.DateTimeField(
        auto_now=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username

    @property
    def is_staff(self):
        return self.is_admin

    def is_member(self, *groups):
        """
        This method used to check group of user.
        If result will be True then User member of this group otherwise not member
        :return: boolean
        """
        return self.groups.filter(name__in=groups).exists()

    @property
    def age(self):
        """
        This abstract method used to calculate age of each User.
        :return: int
        """
        import datetime
        return int((datetime.date.today() - self.dob).days / 365.25)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['username', ]

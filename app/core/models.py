from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
import os
import uuid

class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Custom user model for production login using email instead of username"""
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,

    )
    name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email


class Employee(models.Model):
    first_name = models.CharField(max_length=64, verbose_name="First name")
    last_name = models.CharField(max_length=64, verbose_name="Last name")

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Shift(models.Model):
    """This class could be separated into 3 tables: shift ,store, and shift_choices
        According to shift.csv, only 3 type of fixed shift period.
        as no requirement for editing shift choices and store. For convenience, I use
        the following method.
        Assumption: 1. there are only 3 shift choices:
                        (1, '5:00:00 AM,1:30:00 PM'),
                        (2, '1:00:00 PM,9:30:00 PM'),
                        (3, '9:00:00 PM,5:30:00 AM')
                    2. There are only 3 stores:
                         (1, 'store1'),
                        (2, 'store2'),
                        (3, 'store3')
    """
    employee = models.ForeignKey("Employee", related_name='shifts', on_delete=models.CASCADE)
    date = models.DateField()
    break_time = models.SmallIntegerField(default=60)
    shift_choices = (
        (1, '5:00:00 AM,1:30:00 PM'),
        (2, '1:00:00 PM,9:30:00 PM'),
        (3, '9:00:00 PM,5:30:00 AM')
    )
    shift_type = models.SmallIntegerField(choices=shift_choices, default=1)
    store_choices = (
        (1, 'store1'),
        (2, 'store2'),
        (3, 'store3')
    )
    store_type = models.SmallIntegerField(choices=store_choices, default=1)


def recipe_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('doc/', filename)


class Task(models.Model):
    doc = models.FileField(upload_to='doc/', null=True, verbose_name="Employee Upload List")


from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from app.manager import UserManager


class User(AbstractBaseUser):
    username=None
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    username=models.CharField(max_length=20,unique=True)
    bio=models.CharField(max_length=164,null=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

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
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name','last_name','username']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

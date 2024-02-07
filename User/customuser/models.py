from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager 
from django.contrib.auth.hashers import make_password
from random import randint


class UserProfileManager(UserManager):
    def _create_user(self,email, password, **extra_fields):
        username = email.split("@")[0] + str(randint(0,99999))
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password , **extra_fields: Any) -> Any:
        username = email.split("@")[0] + str(randint(0,99999))
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields: Any) -> Any:
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

# Create your models here.
class UserProfile(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = UserProfileManager()

    

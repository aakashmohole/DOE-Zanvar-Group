from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin, BaseUserManager
from django.db import models


# Create your models here.

# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, first_name="", last_name=""):
        if not email:
            raise ValueError("Users must have an email address")
        
        email = self.normalize_email(email)  # Now this works
        user = self.model(email=email, username=username, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, first_name="", last_name=""):
        user = self.create_user(email, username, password, first_name, last_name)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

# Custom User Model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")

    is_active = models.BooleanField(default=True)  # Required for authentication
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Login with email instead of username
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email
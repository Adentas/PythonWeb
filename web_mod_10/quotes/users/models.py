from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionManager
from django.utils import timezone
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_superuser(username, email, password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionManager):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    data_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.email
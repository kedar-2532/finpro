from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission
# Create your models here.

class UserRole(models.TextChoices):
    ADMIN = 'ADMIN' , 'Admin'
    STAFF = 'STAFF' , 'Staff'
    USER = 'USER' , 'User'

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique = True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=10,
                            choices=UserRole.choices,
                            default=UserRole.USER)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        Group,
        related_name = 'accounts_user_groups',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name = 'accounts_user_permissions',
        blank=True
    )

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email